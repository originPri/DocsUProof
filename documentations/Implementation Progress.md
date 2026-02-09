# Student Information

## Student ID and Name
- Prayankar Bhandari (**H20506**)  
- Aayush Sangroula (**H20631**)  
- Dipanjali Kafle (**H20831**)  
- Prakash Shrestha (**H20332**)  

## Project Supervisor / Advisor
**Dr. Anuj Nepal**

---

# 2. Project Overview

## Project Title
**Rental Checker**

## Summary of the Project
The system enables tenants, landlords, and property managers to upload rental contracts, ask tenancy-related questions, and receive precise, state-specific legal explanations with direct references to official legislation. It simplifies complex legal research, reduces dependency on legal professionals, and promotes transparency in rental practices across Australia.

## Scope of the Project

### Included
- Upload rental contracts in **PDF/DOCX** format  
- Ask tenancy-related questions in simple natural language  
- Access tenancy laws for **NSW, VIC, QLD, SA, WA, and TAS**  
- Identify non-compliant, unfair, or illegal clauses  
- Provide references to official tenancy legislation  
- Deliver explainable, law-backed responses  

### Excluded
- Handling criminal or business agreements  
- Offering professional legal services  
- Including **ACT and NT** laws (future scope)  
- Live chat-based negotiation or dispute escalation  

## Target Users
- Tenants  
- Landlords  
- Property Managers  
- Real Estate Agencies  
- Students, migrants, and first-time renters  

---

# 3. Requirements

## 3.1 Functional Requirements

### High Priority
1. Users can upload rental agreements in PDF/DOCX format  
2. System extracts text and processes legal clauses  
3. Users can ask tenancy-related questions in natural language  
4. System retrieves state-specific tenancy laws  
5. Responses are explainable and include legal citations  
6. Unfair or unlawful clauses are identified and highlighted  

### Medium Priority
1. Admin dashboard to manage legal data ingestion  
2. Clause-level viewing interface  
3. Auto-detection of multi-state jurisdiction  

### Low Priority
1. Export analysis reports as PDF  
2. Light/Dark theme UI  
3. Analysis and report history  

---

## 3.2 User Requirements

The system is designed for multiple stakeholders involved in residential tenancy, each with varying technical expertise.

### User Groups
- Tenants  
- Landlords  
- Property Managers  
- Real Estate Agencies  
- Students, migrants, and first-time renters  

### Details
- **User Distribution:**  
  - High: Tenants and landlords  
  - Medium: Property managers  
  - Low: Agencies and migrants  

- **Geographical Coverage:**  
  - Australia (VIC, NSW, QLD, SA, WA, TAS)  

- **Data Storage Requirements:**  
  - Minimal personal data storage  
  - Secure storage of rental agreements  

- **Network Usage Requirements:**  
  - Moderate bandwidth for document uploads  
  - Support for concurrent multi-user access  

---

## 3.3 Application Requirements

### Applications Needed
- Web Application (Frontend)  
- Backend API (**FastAPI**)  
- Vector Database (**ChromaDB**)  
- Admin Dashboard  

### Data Flow
- User uploads file → backend text extraction → embedding storage  
- User query → embedding search → RAG model → citation-backed response  
- Extracted clauses → contract analysis → highlight violations  

### Special Requirements
- **Latency:** < 3 seconds per query  
- **RAG Accuracy:** > 85% for clause retrieval  
- **Backup:** Local backups for legal data  
- **Throughput:** Support up to 50 concurrent users  

---

## 3.4 Technical Goals (Non-Functional Requirements)

### Scalability
- **Goal:** Handle growing legal databases and user traffic  
- **Trade-off:** Increased cloud resource usage  

### Availability
- **Goal:** 99% API uptime  
- **Trade-off:** Requires reliable hosting infrastructure  

### Network Performance
- **Goal:** Fast query response times  
- **Trade-off:** Buffer and retrieval optimisation required  

### Security
- **Goal:** Secure uploads and user privacy  
- **Trade-off:** Encryption introduces computational overhead  

### Manageability
- **Goal:** Easy updates to laws and models  
- **Trade-off:** Requires modular architecture  

### Usability
- **Goal:** Simple UI for non-technical users  
- **Trade-off:** Feature minimisation for clarity  

### Adaptability
- **Goal:** Support new states and legislation  
- **Trade-off:** Flexible system design needed  

### Affordability
- **Goal:** Low deployment costs  
- **Trade-off:** Limits access to high-end GPU resources  

---

# 4. Analysis and Design

## 4.1 UML and System Models
- Use Case Diagrams

  <img width="876" height="587" alt="image" src="https://github.com/user-attachments/assets/fec21eb8-63c4-4c41-96ea-7cfa135f2da6" />

- Activity Diagrams

  <img width="788" height="1022" alt="image" src="https://github.com/user-attachments/assets/cf4bb1bc-c163-41ed-bbf7-aa67fc4df3b4" />
  
- Data Flow Diagrams

  <img width="975" height="466" alt="image" src="https://github.com/user-attachments/assets/8dc9a9a6-9151-47a9-8c74-c8df17878411" />

- ERD (Entity-Relationship Diagram)

  <img width="940" height="623" alt="image" src="https://github.com/user-attachments/assets/72d3a361-1cc2-401e-9f81-012a5e028040" />

- Class Diagrams

  <img width="1022" height="872" alt="image" src="https://github.com/user-attachments/assets/001bfcf7-40b2-40ea-ad28-d3d56699fd63" />

- Sequence Diagrams

  <img width="940" height="941" alt="image" src="https://github.com/user-attachments/assets/5c2d3288-7343-40c8-84bc-577b2ced39b1" />


---

## 4.2 Design Diagrams
- System Architecture

  <img width="944" height="511" alt="image" src="https://github.com/user-attachments/assets/60e3e81a-f075-46c7-b2f1-b36f222f1c1e" />

- Database Design

  <img width="629" height="474" alt="image" src="https://github.com/user-attachments/assets/80d3e54c-5b39-4322-a765-8761b4addff2" />

- Interface Design

  <img width="975" height="892" alt="image" src="https://github.com/user-attachments/assets/21f885e9-0259-4f1a-a456-523fb6218af1" />


---

## 4.3 UI/UX Design (Screens & Navigation)

### Prototype / Wireframes
[Figma Prototype Link](https://www.figma.com/proto/hz6Q41pmTCJNfICJgCrALo/Web-Application?node-id=1-187&p=f&t=ZWVM8rpGINHSrf2v-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A187)

### Navigation Map
<img width="767" height="975" alt="image" src="https://github.com/user-attachments/assets/0d2d7b5a-e173-4633-8c71-9d13b3943815" />


### Sample Screens

<img width="944" height="540" alt="image" src="https://github.com/user-attachments/assets/03fa373f-86ef-435c-a6ca-d17a30dfbe02" />
 

<img width="944" height="529" alt="image" src="https://github.com/user-attachments/assets/c4cd2710-f76a-4717-8947-0667453c2014" />

<img width="944" height="537" alt="image" src="https://github.com/user-attachments/assets/67c4e9ca-7d1d-4833-9e8d-ba3a605b59a0" />
 
<img width="944" height="537" alt="image" src="https://github.com/user-attachments/assets/3a31404c-c557-454c-ad59-b3d0dacde8dc" />


### Design Principles
The system follows user-centred design principles to ensure accessibility and reliability for all users, including non-technical users:

- Simple and clear interface  
- Consistent layout  
- Transparency to build trust  
- Fully responsive design  

