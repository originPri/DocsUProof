import os
import json
import sys
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException, Query, BackgroundTasks
from fastapi.responses import JSONResponse
from agent.agent import MainAgent
from agent.llm_adapters import MockLLMAdapter, GeminiLLMAdapter
from backend.schemas import Report
from uuid import uuid4
import shutil
import re
import docx
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber

# PDF support
try:
    import pdfplumber
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False
    print("⚠️ pdfplumber not installed. Install with: pip install pdfplumber")

sys.path.append('/app')

RAG_ENABLED = False
rag_retriever = None
try:
    from rag_system.rag_retriever import TenancyLawRetriever
    rag_retriever = TenancyLawRetriever(db_dir="/app/chroma_db")
    RAG_ENABLED = True
    print("✅ RAG system initialized successfully")
except Exception as e:
    print(f"⚠️ RAG system not available: {e}")

# Local storage for uploaded files & reports
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

app = FastAPI(title="Rental Contract Checker (MVP)")

# Enable CORS for React frontend
origins = ["http://localhost:3000", "http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use Gemini for real conversational AI
try:
    agent = MainAgent(llm=GeminiLLMAdapter())
    print("✅ Gemini LLM initialized successfully")
except Exception as e:
    print(f"⚠️ Failed to initialize Gemini: {e}")
    print("Falling back to MockLLMAdapter")
    agent = MainAgent(llm=MockLLMAdapter())

# In-memory report store
REPORTS = {}

# In-memory conversation history
CONVERSATIONS = {}

# Safe RAG helper
def safe_rag_retrieve(query: str, state: str, n_results: int = 3):
    """Retrieve relevant laws safely without crashing if RAG is unavailable"""
    if not RAG_ENABLED or not rag_retriever:
        return []
    try:
        return rag_retriever.retrieve_relevant_laws(query=query, state=state, n_results=n_results)
    except Exception as e:
        print(f"⚠️ RAG retrieval error: {e}")
        return []
@app.get("/")
def read_root():
    return {
        "message": "Rental AI Backend is running with Gemini!",
        "rag_enabled": RAG_ENABLED,
        "pdf_support": PDF_SUPPORT
    }


# Pydantic models
class ChatRequest(BaseModel):
    file_id: str
    message: str
    conversation_history: list = []


# Helper to extract text from different file formats
def extract_text(file_path: str) -> str:
    """Extract text from various file formats"""
    ext = file_path.split(".")[-1].lower()
    
    if ext in ("txt", "text"):
        with open(file_path, "r", encoding="utf-8") as fh:
            return fh.read()
    
    elif ext == "docx":
        try:
            doc = docx.Document(file_path)
            return "\n\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading DOCX: {str(e)}")
    
    elif ext == "pdf":
        if not PDF_SUPPORT:
            raise HTTPException(
                status_code=501, 
                detail="PDF support not available. Install pdfplumber: pip install pdfplumber"
            )
        try:
            text_content = []
            with pdfplumber.open(file_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    page_text = page.extract_text()
                    if page_text:
                        text_content.append(f"--- Page {page_num} ---\n{page_text}")
            
            if not text_content:
                raise HTTPException(
                    status_code=422, 
                    detail="PDF appears to be empty or contains only images. Please use a text-based PDF."
                )
            
            return "\n\n".join(text_content)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading PDF: {str(e)}")
    
    elif ext in ("png", "jpeg", "jpg"):
        raise HTTPException(
            status_code=501, 
            detail="Image OCR not yet implemented. Please convert to PDF or text format."
        )
    
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")


def generate_smart_summary(report: dict, state: str) -> dict:
    """
    Generate a smart summary instead of returning all clauses
    Only highlights problematic areas
    """
    clauses = report.get("clauses", [])
    
    # Categorize issues
    illegal_clauses = [c for c in clauses if c.get("illegal", False)]
    high_risk_clauses = [c for c in clauses if c.get("soft_risk") == "high"]
    medium_risk_clauses = [c for c in clauses if c.get("soft_risk") == "medium"]
    
    # Extract key financial info
    financial = report.get("financial_summary", {})
    rent_amount = financial.get("rent_amount", "Not specified")
    bond_amount = financial.get("bond_amount", "Not specified")
    
    # Overall assessment
    if illegal_clauses:
        overall_verdict = "⚠️ CAUTION - Contains illegal clauses"
        risk_level = "HIGH"
        recommendation = "Do NOT sign this contract without legal advice. Contains clauses that violate tenancy laws."
    elif high_risk_clauses:
        overall_verdict = "⚠️ Review carefully - Contains concerning clauses"
        risk_level = "MEDIUM"
        recommendation = "This contract has some clauses that may be unfair. Review the highlighted issues before signing."
    elif medium_risk_clauses:
        overall_verdict = "✓ Mostly standard - Minor concerns"
        risk_level = "LOW"
        recommendation = "This appears to be a fairly standard contract with some minor points to review."
    else:
        overall_verdict = "✓ Standard contract"
        risk_level = "LOW"
        recommendation = "This appears to be a standard, compliant rental agreement."
    
    # Build issue highlights
    issues = []
    
    for clause in illegal_clauses:
        issues.append({
            "type": "ILLEGAL",
            "severity": "HIGH",
            "title": clause.get("summary", "Illegal clause found"),
            "description": clause.get("plain_english", clause.get("original_text", "")[:200]),
            "why_its_a_problem": ", ".join(clause.get("illegal_reasons", [])),
            "clause_id": clause.get("clause_id"),
            "page_reference": f"Found on page {clause.get('page_num', 'unknown')}"
        })
    
    for clause in high_risk_clauses:
        issues.append({
            "type": "HIGH_RISK",
            "severity": "MEDIUM",
            "title": clause.get("summary", "Concerning clause"),
            "description": clause.get("plain_english", clause.get("original_text", "")[:200]),
            "why_its_a_problem": clause.get("what_this_means", "May not be in your best interest"),
            "clause_id": clause.get("clause_id"),
            "page_reference": f"Found on page {clause.get('page_num', 'unknown')}"
        })
    
    # Quick facts
    quick_facts = {
        "rent": rent_amount,
        "bond": bond_amount,
        "total_upfront": financial.get("total_upfront", "Unknown"),
        "lease_term": report.get("metadata", {}).get("lease_term", "Not specified"),
        "state": state,
        "pages_analyzed": report.get("metadata", {}).get("total_pages", 0)
    }

