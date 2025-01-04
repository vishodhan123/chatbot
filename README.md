# Chatbot Project Documentation

## **Overview**

This project implements a FastAPI-based chatbot that retrieves relevant information from a preprocessed PDF file. It uses FAISS for similarity search, the SentenceTransformer model for embeddings, and integrates seamlessly with GitHub for version control.

---

## **Step-by-Step Guide**

### **1. Prerequisites**

Before starting, ensure you have the following installed on your machine:

- Python 3.8 or above
- pip (Python package manager)
- Git
- SSH Key configured for GitHub (optional but recommended)

### **2. Clone the Repository**

Clone the GitHub repository to your local system:

```bash
git clone git@github.com:vishodhan123/chatbot.git
cd chatbot
```

### **3. Set Up a Virtual Environment**

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

### **4. Install Required Packages**

Install dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### **5. Process the PDF File**

To generate the necessary index files:

1. Navigate to the `config` directory:

   ```bash
   cd config
   ```

2. Place your PDF file in the `config` directory.

3. Run the `ingest.py` script:

   ```bash
   python ingest.py
   ```

   - This script processes the PDF, creates text chunks, and generates the required index files dynamically.

---

### **6. Run the FastAPI Application**

1. Return to the root directory:
   ```bash
   cd ..
   ```
2. Run the FastAPI application:
   ```bash
   python main.py
   ```
3. Access the application in your browser:
   - Swagger UI: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
   - ReDoc: [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

---

### **7. Git Version Control**

#### **Initialize the Repository (If Not Already Done)**

If the repository is not initialized:

1. Initialize Git:
   ```bash
   git init
   ```
2. Add remote origin:
   ```bash
   git remote add origin git@github.com:vishodhan123/chatbot.git
   ```

#### **Standard Workflow for Git**

1. Stage changes:
   ```bash
   git add .
   ```
2. Commit changes:
   ```bash
   git commit -m "Your commit message"
   ```
3. Push changes:
   ```bash
   git push -u origin master
   ```

---

### **8. Testing the Chatbot Endpoint**

1. Use Swagger UI or Postman to test the `/chat` endpoint:

   - Endpoint: `POST /api/v1/chat`
   - Payload:
     ```json
     {
       "query": "What is the leave policy?"
     }
     ```

2. Expected Response:

   ```json
   {
   ```

how

### **9. Directory Structure**

Ensure your directory structure is as follows:

```
chatbot/
├── api/
│   ├── chat_bot_apis/
│   │   ├── __init__.py
│   │   └── teams_chat_bot.py
│   ├── helpers/
│   │   ├── __init__.py
│   │   └── query_helper.py
├── config/
│   ├── database.py
│   ├── ingest.py
├── factory.py
├── main.py
├── requirements.txt
```

---

### **10. Common Issues and Troubleshooting**

#### **Problem: ****`FileNotFoundError`**** for index files**

- Ensure you have run `ingest.py` to generate these files.
- Verify the file paths are being dynamically resolved using `os.path.join` in your `database.py`.

#### **Problem: ****`Permission Denied`**** When Pushing to GitHub**

- Ensure your SSH key is added to GitHub.
- Use `ssh -T git@github.com` to verify your SSH connection.

#### **Problem: ****`FAISS RuntimeError`**

- Ensure that the FAISS index is generated correctly.
- Re-run `ingest.py` if necessary.

---



---


