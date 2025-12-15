# Australian Rental Fairness Checker  
## Project Structure Overview

This document explains the core files and architecture of the Australian Rental Fairness Checker system, including the AI agent, backend services, and the Retrieval-Augmented Generation (RAG) legal knowledge base.

---

## 📁 Agent Folder

### Agent.py
Defines the **MainAgent**, which acts as the central coordinator of the rental-contract analysis system.

**Responsibilities:**
- Takes raw rental contract text as input
- Uses an LLM adapter to extract clauses and metadata
- Applies state-specific tenancy rules via the hybrid rule engine
- Generates a clear, human-readable summary highlighting:
  - Illegal clauses
  - High-risk clauses
  - Medium-risk clauses

**Design Note:**  
This file does **not** contain legal rules or AI model logic. It orchestrates system components to maintain a clean separation between extraction, legal reasoning, and reporting.

---

### llm_adapters.py
Provides an abstraction layer for interacting with Large Language Models (LLMs).

**Key Features:**
- Defines a base `LLMAdapter` interface
- Supports multiple implementations:
  - **MockLLMAdapter**
    - Offline and deterministic
    - Used for development and testing
    - Handles clause extraction and simple rule-based responses
  - **GeminiLLMAdapter**
    - Uses Google Gemini
    - Focused on natural-language explanations and user interaction

**Benefits:**
- Provider independence
- Cost-free testing
- Improved robustness and testability

---

### Prompts.py
Centralizes all prompt templates used by the system.

**Key Prompt:**
- `EXTRACTION_PROMPT`
  - Instructs the LLM to split rental contracts into clauses
  - Returns structured JSON containing:
    - Clause summaries
    - Clause types
    - Numeric values

**Why This Matters:**
- Separates prompt engineering from application logic
- Improves maintainability and transparency
- Allows prompt changes without affecting business logic

---

### rule_engine.py
Implements the **hybrid legal reasoning engine**.

**Capabilities:**
- Contains tenancy rule sets for Australian states (e.g., NSW, VIC)
- Uses heuristic fairness patterns to flag potentially unfair clauses
- Performs:
  - Deterministic legal threshold checks
  - Numeric validations
  - Fairness scoring
  - Optional LLM-assisted reasoning

**Outputs:**
- Clause-level verdicts with scores and explanations
- Aggregated contract-level legal assessment

**Design Goal:**  
Self-contained, auditable, explainable, and suitable for legal review and future expansion.

---

## 📁 Backend Folder

### main.py
Serves as the **central backend entry point** for the application.

**Core Responsibilities:**
- Exposes API endpoints using FastAPI
- Manages file uploads and processing
- Coordinates frontend, AI agent, and legal knowledge base
- Handles system orchestration and application state

**Key Features:**
- CORS configuration for React frontend integration
- Defensive initialization of the RAG system using ChromaDB  
  - Falls back to AI-only reasoning if the legal database is unavailable
- Secure file handling:
  - Supports text and Word documents
  - Reserves PDF and image OCR for future implementation
- Asynchronous background contract analysis to improve responsiveness

---

## 📁 RAG System

### backend_integration.py — Connecting RAG to the Application
Acts as the bridge between the backend/agent and the RAG system.

**Responsibilities:**
- Initializes the RAG retriever once at system startup
- Enhances contract analysis by injecting relevant tenancy laws
- Enriches chat responses with verified legal context
- Enables standalone legal Q&A without requiring contract upload

**Key Functions:**
- `analyze_contract_with_rag`
- `chat_with_rag_context`
- `answer_legal_question`

Includes built-in testing to verify retrieval accuracy and integration reliability.

---

### legal_docs_collector.py — Collecting Raw Government Legal Documents
Responsible for collecting authoritative tenancy laws from Australian government sources.

**Key Tasks:**
- Downloads PDFs or scrapes web-based legislation
- Cleans extracted text to remove UI artifacts and noise
- Splits content into overlapping chunks to preserve context
- Stores embedded chunks in ChromaDB with metadata

Provides testing utilities to verify meaningful legal content retrieval.

---

### legal_docs_to_vector_db.py — Building the Searchable Legal Knowledge Base
Transforms collected legal documents into a structured vector database.

**Process:**
- Chunks and embeds tenancy laws using a semantic model
- Stores embeddings in ChromaDB with state-specific metadata
- Enables semantic search rather than keyword matching

Includes test queries to confirm relevant laws are retrievable.

---

### rag_retriever.py — Finding the Right Laws When Needed
Implements the intelligence layer of the RAG system.

**Key Components:**
- `TenancyLawRetriever` class
- Semantic embedding-based search using ChromaDB
- Optional state-specific filtering
- Context formatting for LLM consumption

**Additional Features:**
- Clause-level legality analysis helpers
- High-level state tenancy overviews
- Example `EnhancedTenancyAgent` demonstrating RAG integration

---

## ✅ Summary
This architecture ensures:
- Clear separation of concerns
- Explainable and auditable legal reasoning
- Robust AI integration with fallback mechanisms
- Scalable backend and legal knowledge retrieval

The system is designed for transparency, maintainability, and future expansion.
