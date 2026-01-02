from sentence_transformers import SentenceTransformer
import numpy as np
import PyPDF2

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
embeddings = []


def read_file(path):
    if path.endswith(".pdf"):
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text

    else:  # txt
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()


def add_document(path):
    text = read_file(path)

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    for chunk in chunks:
        emb = embed_model.encode(chunk)
        documents.append(chunk)
        embeddings.append(emb)


def answer_question(question):
    q = question.lower().strip()

    # ---------- Small talk handling ----------
    if q in ["hi", "hello", "hey"]:
        return "Hi! 👋 How can I help you?"

    if q in ["thanks", "thank you", "thx"]:
        return "You're welcome! 😊"

    if q in ["bye", "goodbye"]:
        return "Bye! 👋"

    # ---------- RAG logic ----------
    if not documents:
        return "Please upload a document first."

    q_emb = embed_model.encode(question)
    scores = np.dot(embeddings, q_emb)
    best = np.argmax(scores)

    context = documents[best]

    # ---------- Smart extraction ----------
    if "email" in q:
        for word in context.split():
            if "@" in word:
                return word.strip()

    if "name" in q:
        return context.splitlines()[0].strip()

    if "phone" in q or "contact" in q:
        for word in context.split():
            if word.replace("+", "").isdigit():
                return word

    # ---------- Fallback: short answer ----------
    return context[:250] + "..."

