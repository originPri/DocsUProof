"""
Pydantic models for request/response validation
"""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ChatRequest(BaseModel):
    prompt: str
    user_id: int | None = None

class UploadResponse(BaseModel):
    success: bool
    doc_id: str
    filename: str
    state: str
    detected_state: Optional[str] = None

class ProcessResponse(BaseModel):
    success: bool
    doc_id: str
    status: str

class QuickFacts(BaseModel):
    rent: str
    bond: str
    state: str
    detected_state: Optional[str] = None
    pages_analyzed: int

class Statistics(BaseModel):
    total_clauses_reviewed: int
    illegal_clauses: int
    high_risk_clauses: int
    medium_risk_clauses: int

class Issue(BaseModel):
    type: str
    title: str
    description: str
    severity: str
    why_its_a_problem: str
    page_reference: str

class AnalysisReport(BaseModel):
    overall_verdict: str
    recommendation: str
    risk_level: str
    quick_facts: QuickFacts
    statistics: Statistics
    issues_found: List[Issue]
    suggested_questions: List[str]

class ReportResponse(BaseModel):
    success: bool
    doc_id: str
    filename: str
    state: str
    analysis: AnalysisReport
    status: str