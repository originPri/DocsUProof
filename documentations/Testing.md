# 1. Unit Testing

## 1.1 Overview
Unit testing was a technique aimed at testing the behaviour of small software units to ensure correctness in internal software logic and functional reliability. Individual elements of backend functionality were isolated and tested under controlled conditions with known inputs to ensure correct outputs without relying on database or network communications.

Some of the key modules tested included:
- PDF text extraction
- Clause classification logic
- Legal text embedding generation
- Jurisdiction detection

These tests ensured that each function could handle valid inputs correctly and fail safely in invalid scenarios. Edge-case handling was also tested to prevent runtime crashes or unstable system states.

The successful execution of unit tests demonstrated that the fundamental components worked correctly and were ready to be integrated into the complete system pipeline.

## 1.2 Unit Testing Objectives
The main objectives of unit testing were:
- Validate correctness of individual functions
- Ensure stable edge-case handling
- Prevent runtime crashes
- Verify predictable and expected outputs
- Build a strong foundation for system integrity testing

## 1.3 Unit Testing Approach
Unit tests were implemented on isolated backend functions using controlled test inputs. Each function was tested independently, without interaction with the database or frontend components. Expected results were predefined and compared against actual system behaviour.

Both positive and negative test cases were performed, including:
- Valid document processing
- Invalid file handling
- Empty input protection
- Illegal clause detection
- Jurisdiction parsing accuracy

Jurisdiction parsing accuracy evaluates whether the system correctly identifies the applicable legal jurisdiction based on the rental agreement text.

## 1.4 Unit Test Cases

| Test ID | Component | Description | Input | Expected Result | Actual Result | Status |
|-------|----------|-------------|-------|----------------|---------------|--------|
| UT_001 | PDF Parser | Extract text from valid PDF | Valid rental PDF | Text extracted | Text extracted | PASS |
| UT_002 | PDF Parser | Handle corrupted PDF | Corrupted file | Error returned | Error handled | PASS |
| UT_003 | Clause Detector | Detect illegal clause | Illegal clause text | Clause flagged | Clause flagged | PASS |
| UT_004 | Jurisdiction Engine | Detect NSW state | NSW contract | NSW detected | NSW detected | PASS |
| UT_005 | Embedding Engine | Generate embeddings | Legal text input | Vector created | Vector created | PASS |
| UT_006 | Input Validator | Empty upload handling | Empty file | Error message | Error displayed | PASS |

## 1.5 Example Unit Test Code
<img width="908" height="133" alt="image" src="https://github.com/user-attachments/assets/cc6af3fb-1a62-4fd8-b0ae-2d875de75c31" />
<img width="775" height="167" alt="image" src="https://github.com/user-attachments/assets/04d74cd1-5bcd-4d6b-8e31-c6c6dc08b073" />
<img width="775" height="138" alt="image" src="https://github.com/user-attachments/assets/37139854-40c4-4d91-846c-3d7a59cbe39f" />




## 1.6 Unit Testing Results
All unit tests were executed successfully with no critical failures observed. Backend modules exhibited consistent behaviour across all tested scenarios. Edge cases were handled effectively, and the system did not crash when invalid inputs were provided.

These results confirmed that the individual components were stable and suitable for integration into the overall system architecture.

## 1.7 Unit Testing Conclusion
Unit testing established a strong reliability baseline for the system by confirming that individual modules function correctly and independently. This significantly reduced integration risks and increased confidence in the backend processing pipeline. The consistency of test results indicates that the system’s internal logic is stable and robust.

---

# 2. Integration Testing

Integration testing was conducted to verify that major system components—frontend, backend API, and database—operate together as a unified system. This testing phase focused on inter-component communication, service startup reliability, and data flow across the architecture.

System logs and runtime behaviour were monitored to ensure proper service initialization and interaction.

## 2.1 Rental_Postgres Testing
The PostgreSQL integration test validated database startup, connection stability, and readiness to handle backend requests. On system startup, PostgreSQL loaded the existing database instance and began listening on the configured ports without errors.

Log outputs confirmed successful database initialization and availability for connections. The backend connected reliably and performed transactional operations without failure, ensuring data integrity.

This test confirmed that the database integration was successful and provided a stable storage layer for the application.

## 2.2 Rental_Frontend Testing
Frontend integration testing verified the build and runtime behaviour of the React-based user interface. The application compiled successfully via Webpack, and the development server started without errors.

The frontend was accessible via a local browser and properly connected to the backend API. Core user interactions—including document upload, query submission, and response display—were tested and confirmed to function correctly.

Minor deprecation warnings were observed but did not affect runtime performance or user experience.

## 2.3 Rental_Backend Testing
Backend integration testing assessed server startup, database connectivity, and API readiness. The FastAPI server was launched successfully using Uvicorn and connected to PostgreSQL without issues.

Database migrations completed successfully, and the backend handled requests related to document processing, clause analysis, and AI-generated responses. Non-critical telemetry warnings did not affect system functionality.

This confirmed that the backend acts as a stable and reliable processing layer.

## 2.4 End-to-End Chat Processing Testing
This test validated the full AI chat workflow from frontend input to backend processing and response generation. User queries submitted through the frontend were correctly processed by the backend, which retrieved relevant legal content from the vector database and generated comprehensible responses.

System logs confirmed successful user identification, document retrieval, AI processing, and HTTP responses. This demonstrated seamless interaction between all components and verified that the Retrieval-Augmented Generation (RAG) pipeline works correctly in a real-world environment.

## 2.5 Document Upload and Database Testing
This integration test verified the document ingestion pipeline. Uploaded rental agreements were successfully processed, stored, and validated within the database.

Logs confirmed successful text extraction, jurisdiction detection, database record creation, commit operations, and post-save verification. Retrieved documents retained full content integrity.

This demonstrated reliable handling of large legal documents and confirmed successful integration between upload interface, backend processing, and PostgreSQL storage.

---

# 3. Test Cases and Results

The following test cases evaluated the core functional behaviour of the AI Rental Contract Fairness Checker. These tests covered document upload, text extraction, clause detection, jurisdiction identification, legal query processing, performance, and system stability.

All tests were conducted under controlled conditions to ensure accurate handling of valid and invalid inputs.

## 3.1 Functional Test Cases

| Test Case ID | Scenario | Description | Preconditions | Expected Result | Actual Result | Status | Remarks |
|-------------|----------|-------------|---------------|----------------|---------------|--------|---------|
| TC_001 | Document Upload | Upload valid rental PDF | User logged in | File accepted and analysis starts | Uploaded and processed | PASS | Works as expected |
| TC_002 | Document Upload | Upload unsupported file | User logged in | Error message shown | Error displayed | PASS | Validation working |
| TC_003 | Text Extraction | Extract text from PDF | Valid PDF uploaded | Readable text extracted | Text extracted | PASS | No extraction errors |
| TC_004 | Clause Detection | Detect unfair clause | Illegal clause present | Clause highlighted with explanation | Clause flagged | PASS | Accurate detection |
| TC_005 | Jurisdiction Detection | Auto-detect state law | NSW contract | NSW identified | NSW law retrieved | PASS | Correct mapping |
| TC_006 | Legal Query | Ask tenancy question | User logged in | Law retrieved with citation | Citation-backed answer | PASS | RAG working |
| TC_007 | Citation Accuracy | Verify citation | Legal answer generated | Citation matches law | Verified | PASS | Explainability confirmed |
| TC_008 | Performance | Large contract analysis | 30-page document | Completed < 5 seconds | 3.1 seconds | PASS | Acceptable performance |
| TC_009 | Error Handling | Upload corrupted PDF | Corrupted file | Error without crash | Error handled | PASS | Stable system |
| TC_010 | Multi-user Access | Concurrent queries | 2 users active | Requests handled | All processed | PASS | Scalable |

---


