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
git clone DocsUProof.git
cd DocsUProof

