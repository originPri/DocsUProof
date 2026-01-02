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


