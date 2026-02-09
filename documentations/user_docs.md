# Rental AI System  
## User Manual  
**Version 1 | January 2026**

---

## Abstract
This document presents a complete user manual for the **Rental AI System**, an AI-powered platform designed to analyse rental contracts and answer tenancy-related questions. The system allows users to upload rental agreements, identify potentially unfair clauses, and receive explainable legal guidance based on state-specific tenancy regulations.

This manual includes installation instructions, system access requirements, step-by-step usage guidelines, and troubleshooting support to ensure users can operate the system easily and effectively.

---

## Table of Contents
1. Introduction  
   1.1 Purpose of This Manual  
   1.2 Intended Audience  
   1.3 System Overview  

2. Installation Guide  
   2.1 System Requirements  
   2.2 Installation Steps  

3. System Access  
   3.1 Access Channels  
   3.2 Browser Requirements  

4. User Guide  
   4.1 Login & Signup  
   4.2 Upload Rental Contract  
   4.3 AI Analysis Output  
   4.4 Ask Questions About the Contract  
   4.5 Chat Features  

5. Help Manual / Troubleshooting  
   5.1 Common Issues  
   5.2 Support  

6. Security & Privacy Notes  

7. Conclusion  

---

## 1. Introduction

### 1.1 Purpose of This Manual
This manual assists users in installing, accessing, and using the Rental AI System. It provides guidance on uploading rental agreements, interacting with the AI assistant, and interpreting system feedback. The documentation is designed to make the system user-friendly, even for users without technical expertise.

### 1.2 Intended Audience
This manual is intended for:
- Tenants reviewing rental agreements  
- Property managers and landlords  
- Students and first-time tenants  
- Housing advisors and legal interns  
- Individuals seeking tenancy-related advice  

No technical background is required to use the system.

### 1.3 System Overview
The Rental AI System is a web-based AI solution that analyses rental agreements using **Retrieval-Augmented Generation (RAG)**. Users upload a PDF rental contract and ask questions related to the document. The system extracts text, compares it with tenancy legislation, and provides explainable legal responses.

**Key Features**
- Rental contract upload and analysis  
- Clause highlighting and risk identification  
- State-based legal retrieval  
- AI-powered chat interface  
- Secure document storage  
- Chat history tracking  

---

## 2. Installation Guide

### 2.1 System Requirements
Before installing the system, ensure the following are installed:
- Docker Desktop  
- Git  
- Python 3.11 or higher  
- Node.js (for frontend)  
- Active internet connection  

### 2.2 Installation Steps

#### Step 1: Install Docker
Download Docker Desktop from:  
- https://www.docker.com/products/docker-desktop  

Install, log in, and start Docker.

#### Step 2: Clone the Repository
```bash
git clone https://github.com/originPri/DocsUProof.git

cd DocsUProof
```

#### Step 3: Start Backend Services

```bash
cd backend
docker compose up --build
```

This will start the following services:

- **PostgreSQL database**
- **Backend API**
- **AI processing services**

#### Step 4: Start Frontend
```bash
cd frontend
npm install
npm start
```

#### Step 5: Access the Application
Open a web browser and navigate to:

```arduino
http://localhost:3000
```

## 3. System Access

### 3.1 Access Channels
Users can access the system via:
- Web browser interface  
- Local development server  

### 3.2 Browser Requirements
Recommended browsers:
- Google Chrome  
- Microsoft Edge  
- Mozilla Firefox  

No mobile installation is required.

---

## 4. User Guide

### 4.1 Login & Signup
When opening the system:
- Click **Login / Signup**
- Log in using:
  - Google account  
  - Email authentication  

Upon successful login, the user dashboard is displayed.
<img width="803" height="459" alt="image" src="https://github.com/user-attachments/assets/34e73ae4-4ab7-4a48-83e0-9bc4712c4c49" />
<img width="803" height="503" alt="image" src="https://github.com/user-attachments/assets/f9945eae-700d-48b8-8139-94f6d78c9ca5" />



---

### 4.2 Upload Rental Contract
1. Select your **State/Territory**  
2. Click **Upload Document**  
3. Choose a rental agreement PDF  
4. Click **Analyze**  

The system automatically extracts and processes the contract.
<img width="986" height="561" alt="image" src="https://github.com/user-attachments/assets/03683143-e2e1-4df6-a497-c75ac6233928" />


---

### 4.3 AI Analysis Output
After upload:
- Clauses are analysed  
- Risky or unfair terms are highlighted  
- Legal explanations are displayed  

Users receive a clear and readable summary of contract issues.
<img width="986" height="563" alt="image" src="https://github.com/user-attachments/assets/4638fa7b-10c5-4242-8ba6-24c44d382128" />


---

### 4.4 Ask Questions About the Contract
Using the chat box, users can ask questions such as:
- *“Is this bond legal?”*  
- *“Can the landlord increase rent?”*  
- *“Is early termination allowed?”*  

The AI responds based on the uploaded contract and relevant tenancy laws.
<img width="847" height="483" alt="image" src="https://github.com/user-attachments/assets/44e8bc66-0071-478a-8de6-51901005964e" />

<img width="851" height="484" alt="image" src="https://github.com/user-attachments/assets/ddf68040-2de6-43de-bbdf-f9e45432a7ef" />




---

### 4.5 Chat Features
- Start a new session using the **New Chat** button  
- Chat history is saved automatically  
- Users can review previous chats  
- Logout option is available in the sidebar


<img width="986" height="565" alt="image" src="https://github.com/user-attachments/assets/ee33d9e5-468e-4b4c-b3f2-f0894a747cf9" />


---

## 5. Help Manual / Troubleshooting

### 5.1 Common Issues

**File Upload Fails**
- Ensure the file:
  - Is in PDF format  
  - Is not corrupted  
  - Is within the size limit  

**No Response from AI**
- Check internet connection  
- Restart backend server  
- Refresh the browser  

**Slow Analysis**
- Large files may take several seconds  
- This is expected behaviour  

**Login Issues**
- Log out and log back in  
- Clear browser cache  
- Google authentication may require re-login  

---

### 5.2 Support
If issues persist:
- Restart Docker containers  
- Rebuild backend services  
- Contact the system administrator

---

## 6. Security & Privacy Notes
- Documents are stored securely  
- User sessions are private  
- No data is shared externally  
- Uploaded files are used only for analysis  

---

## 7. Conclusion
The Rental AI System simplifies the understanding of rental contracts through AI-powered legal analysis. This user manual enables users to install, operate, and troubleshoot the platform with ease. By providing transparent legal insights, the system empowers renters and promotes fairness in housing agreements.

