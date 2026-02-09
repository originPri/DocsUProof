# IT3090.10 – Project Proposal

---

## Student Details

- **H20506** – Prayankar Bhandari  
- **H20631** – Aayush Sangroula  
- **H20831** – Dipanjali Kafle  
- **H20332** – Prakash Shrestha  

---

## Project Supervisor / Advisor
**Dr. Anuj Nepal**

---

## Project Title
**DocsUProof**

---

## Purpose of the Project
DocsUProof is an **Australian Tenancy Law Analysis System**. Upon completion, the system will allow users to analyse rental agreements and tenancy-related questions using an AI-driven approach that extracts and interprets Australian tenancy laws on a **state-by-state basis**.

Currently, such analysis requires extensive manual legal research and professional legal assistance, which is time-consuming and costly. DocsUProof aims to automate this process by allowing users to submit rental agreements and ask **natural-language questions**, receiving **jurisdiction-aware, legally grounded answers** supported by official Australian tenancy legislation.

---

## Business Objectives of the Project

| No. | Business Goal | Evidence of Goal Achieved |
|----|--------------|---------------------------|
| 1 | Provide quick access to Australian tenancy laws | Users can ask state-specific questions (NSW, VIC, QLD, SA, WA, TAS) in natural language |
| 2 | Reduce dependency on legal professionals for basic tenancy questions | Users receive accurate legal explanations without manual research |
| 3 | Detect unfair or illegal clauses in rental agreements | System flags clauses violating legal limits (bond, rent, increases, notices) |
| 4 | Ensure explainable and trustworthy AI responses | AI answers reference official legislation and retrieved legal text |
| 5 | Ensure scalability and future expansion | Architecture supports adding new states (ACT, NT) and law updates |

---

## Scope of the Project

### In Scope

#### System Functions
- Upload rental agreements (PDF, DOCX)  
- Ask natural-language tenancy questions  
- Receive state-specific legal answers  
- Compare contract clauses with legislation  
- Identify potentially unfair or illegal terms  
- Provide legally grounded explanations  
- Handle jurisdiction-specific queries  

#### System Documentation
- Project Proposal  
- System Design Specification  
- Test Cases and Test Results  
- Final Project Report  

#### Training
End-user training on:
- Uploading rental contracts  
- Asking tenancy-related questions  
- Interpreting system responses  

#### Training Materials
- User Guide  
- Step-by-step usage documentation  

#### User Manual
- System configuration  
- Python-based backend  
- FastAPI services  
- ChromaDB vector storage  
- Sentence-Transformers embeddings  
- PDF ingestion and legal data processing  
- Configuration files for:
  - Data sources  
  - Embedding models  
  - Vector database persistence  

#### System Maintenance
- Maintenance and update documentation  

---

## Sprints, Epics, Stories, and Tasks

### Epics
- Legal Data Acquisition  
- RAG System Development  
- Explainable AI Integration  
- Frontend and Backend Integration  
- Testing and Validation  

### Sample User Stories
- As a tenant, I want to know whether my bond amount is legal.  
- As a landlord, I want to ensure my lease complies with tenancy laws.  
- As a user, I want all results verified using official legal sources.  

---

## Budget and Timeframe

- **Budget:** No financial budget (academic project)  
- **Time Commitment:** Minimum of 10 hours per week per group member  
- **Timeframe:** Defined by the academic semester  

Milestones and deliverables may be adjusted with agreement from all group members.

---

## Project Milestones

| Milestone | Deliverable | Expected Date |
|---------|-------------|---------------|
| Project Startup | Initial project concept paper | Week 1–3 |
| Project Proposal | Project proposal | Week 3–6 |
| Solution Requirements | Requirements & test strategy | Week 4 |
| Solution Design | Architecture & design documents | Week 5 |
| Prototype | Core RAG system | Week 6 |
| Iteration 1 | Legal data ingestion, test cases | Week 7 |
| Iteration 2 | Contract analysis, test results | Week 8 |
| Iteration 3 | Testing and refinement | Week 9 |
| Final Release | Full system and documentation | Week 10 |
| Project Completion | Final submission | Week 11 |

---

## Project Schedule

### Gantt Chart (High-Level Tasks)
1. Project initiation and planning  
2. Legal data collection (all states)  
3. Data cleaning and PDF text extraction  
4. RAG architecture and vector database setup  
5. Embedding and retrieval logic  
6. Explainable AI (citations and sources)  
7. Backend API development  
8. Frontend UI development  
9. System testing and validation  
10. Documentation and final submission  

### WBS
<img width="975" height="633" alt="image" src="https://github.com/user-attachments/assets/e84476db-1646-452f-86c0-9e18fb9f63ee" />


### PERT Chart

<img width="850" height="385" alt="image" src="https://github.com/user-attachments/assets/4325f94c-1d60-477a-8617-5e95ab06b2f9" />


---

## Risk Management

### Assumptions
- Government legislation websites remain accessible  
- Use of PDFs is legally permitted  
- Required Python libraries remain supported  
- Supervisor feedback is provided as scheduled  

### Dependencies
- Government legislation portals  
- Python open-source libraries  
- Internet access  
- Academic semester schedule  

---

## Risk Rating Table

| ID | Risk | Likelihood (1–3) | Severity (1–3) | Ranking (L×S) |
|----|------|------------------|---------------|---------------|
| R1 | Scraping failures | 2 | 2 | 4 |
| R2 | Legal text changes | 2 | 3 | 6 |
| R3 | Dependency conflicts | 3 | 2 | 6 |
| R4 | Time constraints | 2 | 2 | 4 |

---

## Risk Mitigation Table

| ID | Risk Event | Mitigation Strategy |
|----|-----------|---------------------|
| R1 | Scraping failures | Manual PDF uploads |
| R2 | Law updates | Modular data ingestion |
| R3 | Library conflicts | Version pinning |
| R4 | Time constraints | Iterative scope control |

---

## Technical and Resource Requirements

### Development Platform
- Windows  
- Python 3.11  
- Visual Studio Code  
- GitHub  

### Implementation Platform
- FastAPI backend  
- ChromaDB vector store  
- Sentence-Transformers embeddings  
- Playwright for legal data scraping  
- PDF parsing and text extraction tools  

