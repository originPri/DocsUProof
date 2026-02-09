## Project Concept and Summary

Renting a house or apartment can be particularly stressful for **students, migrants, and first-time renters**, especially when rental agreements contain complex legal terminology. Many individuals enter lease agreements without fully understanding hidden costs, unfair penalties, or clauses that may even violate Australian tenancy laws. This lack of clarity can lead to financial loss, unnecessary stress, and an imbalance of power between landlords and renters.

The **AI Rental Fairness Checker** is an online tool designed to help renters analyse lease agreements **before signing**. The system allows users to upload a PDF or image of their rental contract. The uploaded document is processed to extract text, split into individual clauses, and analysed using a **Large Language Model (LLM)** combined with a **rule-based tenancy law engine**. This approach helps identify potentially unfair, misleading, or illegal clauses.

Risky provisions are flagged, categorised (e.g. fees, termination, repairs, privacy), and explained in **clear, simple, and easy-to-understand language**. The system is intended to empower users with knowledge and confidence when reviewing rental agreements.

The application will be developed using a **Python-based backend API** and a **React, HTML, and CSS frontend**, supported by an AI model for natural language processing. The final web application aims to be functional, well-designed, and accessible, promoting transparency, trust, and fair rental practices. While the system does not replace professional legal advice, it provides renters with a strong starting point to understand their rights and ask informed questions.

---

## Key Objectives

- Design and develop a **responsive web application interface** compatible with desktop and mobile devices, featuring a simple workflow for uploading and reviewing analysed contracts.

- Implement **secure user authentication and data storage**, ensuring uploaded rental contracts are protected using encryption and role-based access control.

- Develop an **AI and rule-based analysis engine** to automatically classify clauses by:
  - Risk level (low / medium / high)  
  - Category (fees, termination, maintenance, privacy, etc.)  
  in alignment with Australian tenancy guidelines.

- Create a **document processing system** capable of accepting PDFs and images, performing OCR where necessary, and achieving reliable text extraction on at least **90–95% of test contracts**.

- Enhance result presentation with **visual highlighting** and provide a downloadable report summarising key risks and recommendations, enabling users to consult tenancy support services or legal professionals.

---

## Proposed Technology and Resources

### Tools
- **GitHub** – Version control and collaboration  
- **Visual Studio Code (VS Code)** – Development and deployment  
- **Figma** – UI/UX design and prototyping  

### Front-End
- **React, HTML, CSS**  
  Used to build a responsive and interactive user interface with highlighted clauses and clear risk summaries.

### Back-End
- **Python**  
  Used to handle file uploads, API communication, and backend processing efficiently.

### Artificial Intelligence
- **OpenAI or similar Large Language Models (LLMs)**  
  Used to analyse contract language, identify unfair patterns, and map clauses to defined risk categories.

### Database
- **PostgreSQL or MySQL**  
  Used to securely store user accounts, contract metadata, analysis results, and audit records.

