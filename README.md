Chatbot Project Documentation

Overview

This project implements a FastAPI-based chatbot that retrieves relevant information from a preprocessed PDF file. It uses FAISS for similarity search, the SentenceTransformer model for embeddings, and integrates seamlessly with GitHub for version control.

Step-by-Step Guide

1. Prerequisites

Before starting, ensure you have the following installed on your machine:

Python 3.8 or above

pip (Python package manager)

Git

SSH Key configured for GitHub (optional but recommended)

2. Clone the Repository

Clone the GitHub repository to your local system:

git clone git@github.com:vishodhan123/chatbot.git
cd chatbot

3. Set Up a Virtual Environment

Create a virtual environment:

python -m venv .venv

Activate the virtual environment:

On Windows:

.venv\Scripts\activate

On macOS/Linux:

source .venv/bin/activate

4. Install Required Packages

Install dependencies listed in requirements.txt:

pip install -r requirements.txt

5. Process the PDF File

To generate the necessary index files:

Navigate to the config directory:

cd config

Place your PDF file in the config directory.

Run the ingest.py script:

python ingest.py

This script processes the PDF, creates text chunks, and generates the required index files dynamically.

6. Run the FastAPI Application

Return to the root directory:

cd ..

Run the FastAPI application:

python main.py

Access the application in your browser:

Swagger UI: http://127.0.0.1:8080/docs

ReDoc: http://127.0.0.1:8080/redoc

7. Git Version Control

Initialize the Repository (If Not Already Done)

If the repository is not initialized:

Initialize Git:

git init

Add remote origin:

git remote add origin <repo>

Standard Workflow for Git

Stage changes:

git add .

Commit changes:

git commit -m "Your commit message"

Push changes:

git push -u origin master

8. Testing the Chatbot Endpoint

Use Swagger UI or Postman to test the /chat endpoint:

Endpoint: POST /api/v1/chat_bot

Payload:

{
  "query": "What is the leave policy?"
}

Expected Response:

{
    "query": "What is the leave policy?",
    "results": [
        {
            "score": 0.85,
            "chunk": "The company offers 12 days of paid leave per year..."
        },
        ...
    ]
}
