# Final Project Report  
## Project Title: AI Rental Checker

---

## 1. Project Summary
This project focused on the development of an **AI-powered web-based system** designed to analyse Australian residential rental contracts and respond to tenancy-related queries using an **explainable Retrieval-Augmented Generation (RAG) architecture**. The system enables tenants, landlords, and property managers to upload rental contracts or submit natural-language questions and receive accurate, **state-specific legal clarifications** supported by official tenancy legislation.

The primary objective of the project was to improve **transparency and fairness** in rental agreements by identifying potentially unfair, unlawful, or non-compliant clauses and presenting them in an easy-to-understand format. The system automates legal clause analysis and legislative retrieval, reducing dependence on legal professionals for basic tenancy understanding and minimizing manual legal research.

Overall, the project demonstrates the practical application of **AI, natural language processing (NLP), and explainable systems** to address a real-world social and legal problem.

---

## 2. Methodology
An **iterative and incremental development approach** was adopted to allow continuous refinement based on testing results and supervisor feedback. The development process was divided into the following stages:

### 2.1 Requirements Analysis and Planning
Tenancy law use cases were analysed to identify both functional and non-functional requirements. The project scope was clearly defined to focus on **residential tenancy laws** across major Australian states, including:
- NSW  
- VIC  
- QLD  
- SA  
- WA  
- TAS  

### 2.2 System Design
A modular system architecture was designed, consisting of:
- A web-based user interface  
- Backend API developed using **FastAPI**  
- **ChromaDB** for legal text embeddings  
- A retrieval, reasoning, and citation-based **explainable RAG pipeline**

UML diagrams, system architecture diagrams, and UI wireframes were created to guide the implementation process.

### 2.3 Implementation
Key implementation steps included:
- Collection of legal records from official government tenancy law portals  
- Text extraction and preprocessing of legal documents and uploaded rental contracts  
- Generation of embeddings using **Sentence-Transformers**  
- Development of a RAG-based AI pipeline to retrieve relevant legal provisions and produce explainable responses  
- Integration of the frontend with backend APIs to support document upload, query handling, and result visualisation  

### 2.4 Testing and Validation
Functional testing was conducted to verify:
- Accurate clause detection  
- Correct jurisdiction identification  
- Proper legal citation generation  

Performance testing confirmed acceptable response latency and output quality. Based on testing outcomes, iterative improvements were applied throughout development.

---

## 3. Challenges Encountered
Several challenges were faced during the project:

- **Legal Data Complexity**  
  Australian tenancy laws vary significantly between states, requiring careful separation, tagging, and retrieval of jurisdiction-specific legislation.

- **PDF Text Extraction Issues**  
  Variations in formatting across rental agreements and legal documents created difficulties in accurate text extraction.

- **Explainability of AI Responses**  
  Ensuring AI-generated responses were not only correct but also explainable and supported by official legal references required careful RAG pipeline design.

- **Time Constraints**  
  Academic deadlines necessitated strict scope control and prioritisation to balance system completeness, accuracy, and documentation.

These challenges were mitigated through modular system design, fallback manual uploads, version-controlled dependencies, and continuous scope refinement within the iterative development process.

---

## 4. Results and Outcomes
The final system successfully achieved its intended objectives:

- Users can upload rental agreements (PDF/DOCX) and ask tenancy-related questions  
- The system accurately retrieves **state-specific tenancy laws** and identifies unfair or illegal clauses  
- AI-generated explanations are clear, justified, and supported by official legal references  
- The modular architecture allows easy expansion to additional jurisdictions (e.g., ACT, NT) and future legal updates  

The project demonstrates that the AI solution is **scalable, functional, and socially beneficial**, helping to raise renter awareness and promote fairness in rental agreements. It also highlights the effective integration of AI, legal document processing, and explainable decision-support systems.

