
# 🤖 AI Chatbot Assistant (RAG-based)

An AI-powered chatbot assistant that allows users to **upload documents (PDF/Text)** and **ask questions** in a conversational, web-based interface.  
The chatbot retrieves relevant information from uploaded documents using embeddings and responds intelligently.


https://github.com/user-attachments/assets/6bd338ff-c0f1-42a9-a9c9-2ea6272227a6


The project is fully **Dockerized**, so anyone can run it without cloning the repository.

---

## 🚀 Features

- 💬 Chatbot-style conversational UI
- 📄 Upload PDF or text documents
- 🔍 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI backend
- 🌐 Web interface (HTML + CSS)
- 🐳 Docker support for easy sharing and deployment

---

## 🖥️ Demo Usage

1. Upload a document (PDF or text)
2. Ask questions in natural language
3. Get answers extracted from the uploaded document

---

## 🐳 Run Using Docker (Recommended)

No cloning required.

```bash
docker pull balaji1618/ai-chatbot:latest
docker run -p 8000:8000 balaji1618/ai-chatbot:latest
````

Open in browser:

```
http://localhost:8000
```

---

## 🛠️ Run Locally (For Development)

```bash
pip install -r requirements.txt
python -m uvicorn src.app:app --reload
```

---

## 📂 Project Structure

```
ai-chatbot/
├── src/
│   ├── app.py            # FastAPI application
│   ├── pipeline.py       # RAG pipeline & embeddings
│   ├── templates/
│   │   └── index.html    # Chat UI
│   └── static/
│       └── style.css
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧠 Tech Stack

* Python
* FastAPI
* Jinja2 (Frontend templating)
* Sentence Transformers / Embeddings
* PyPDF2
* Docker

---

## 🎯 Use Cases

* Resume / document Q&A
* Knowledge assistant
* Study material chatbot
* Internal document assistant

---

## 👤 Author

**Balaji Jayaprakash**
MSc Robotics – TU Delft
Robotics | AI | Machine Learning

---

## 📌 Notes

* Ensure a document is uploaded before asking questions
* Large PDFs may take time to process initially
* Designed for learning, demos, and personal projects

---

