import os
import json
import PyPDF2

# Folders
RAW_DIR = r"C:\Users\balaj\Desktop\data\raw_docs"        # where PDFs/TXTs are
OUT_FILE = r"C:\Users\balaj\Desktop\data\processed\chunks.json"  # output JSON

# Chunking settings
CHUNK_SIZE = 300
OVERLAP = 50


def read_pdf(file_path):
    """Read PDF and return all text"""
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def chunk_text(text, size, overlap):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    idx = 0

    while start < len(text):
        end = start + size
        chunk = text[start:end]

        chunks.append({
            "chunk_id": idx,
            "text": chunk
        })

        idx += 1
        start += size - overlap

    return chunks


def ingest_documents():
    """Ingest all TXT and PDF files in RAW_DIR and create JSON chunks"""
    all_chunks = []

    for filename in os.listdir(RAW_DIR):
        path = os.path.join(RAW_DIR, filename)

        if filename.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        elif filename.endswith(".pdf"):
            text = read_pdf(path)
        else:
            continue  # skip unsupported files

        chunks = chunk_text(text, CHUNK_SIZE, OVERLAP)

        for chunk in chunks:
            all_chunks.append({
                "chunk_id": f"{filename}_{chunk['chunk_id']}",
                "source": filename,
                "text": chunk["text"]
            })

    # ensure output folder exists
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"Ingested {len(all_chunks)} chunks from {RAW_DIR}")
    print(f"Saved JSON to {OUT_FILE}")


if __name__ == "__main__":
    ingest_documents()
