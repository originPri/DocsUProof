# DocsUProof

**DocuProof** is an AI-powered contract verification web app that helps users quickly understand their rental agreements and other legal documents. Upload a PDF, Word, text, or image file and DocuProof will extract the text, analyse clauses, highlight risks, and generate a clear, human-friendly summary.

---

##  Features

- **Multi-format upload**: Supports PDF, Word, plain text, and image-based documents.
- **Built-in OCR**: Automatically converts scanned or photo-based contracts into text.
- **AI-powered analysis** (Gemini API):
  - Extracts key clauses
  - Highlights potential risks and red flags
  - Detects missing or unusual terms
  - Generates plain-language summaries
- **Chat-style interface**: Interact with your contract like a conversation.
- **Swagger UI**: Test and inspect backend API endpoints for the full processing pipeline.

---

##  High-Level Architecture

1. **Frontend (Web App)**
   - Landing page introducing DocuProof
   - Chat page where users upload contracts and view analysis

2. **Backend**
   - File upload & validation
   - OCR service integration for image-based documents
   - Text preprocessing and cleaning
   - Calls Gemini API for clause extraction & analysis
   - Returns structured analysis back to the frontend

3. **Developer Tools**
   - Swagger UI for API documentation and testing

---

##  Tech Stack (Example)

- **Frontend**: React 
- **Backend**: Python (FastAPI)
- **AI**: Gemini API
- **OCR**
- **API Docs**: Swagger / OpenAPI

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/DocsUProof.git
cd DocuProof
