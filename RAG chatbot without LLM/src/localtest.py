import os
import json
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --- File paths ---
CHUNKS_FILE = r"C:\Users\balaj\Desktop\data\processed\chunks.json"
EMBED_FILE = r"C:\Users\balaj\Desktop\embeddings\index.pkl"

# --- Step 1: Load chunks ---
with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks")

# --- Step 2: Load or create embeddings ---
if os.path.exists(EMBED_FILE):
    with open(EMBED_FILE, "rb") as f:
        chunks = pickle.load(f)
    print(f"Loaded embeddings from {EMBED_FILE}")
else:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    for chunk in chunks:
        chunk["embedding"] = model.encode(chunk["text"]).tolist()
    os.makedirs(os.path.dirname(EMBED_FILE), exist_ok=True)
    with open(EMBED_FILE, "wb") as f:
        pickle.dump(chunks, f)
    print(f"Saved embeddings to {EMBED_FILE}")

# --- Step 3: Ask a question locally ---
model = SentenceTransformer("all-MiniLM-L6-v2")
question = "What is my full name?"
query_emb = model.encode(question)

# Compute cosine similarity with all chunks
sims = [cosine_similarity([query_emb], [chunk["embedding"]])[0][0] for chunk in chunks]
best_idx = np.argmax(sims)

print("\nTop similarity score:", sims[best_idx])
print("\nBest matching chunk text:\n")
print(chunks[best_idx]["text"])
