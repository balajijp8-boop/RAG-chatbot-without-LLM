import os
import json
import pickle
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = r"C:\Users\balaj\Desktop\data\processed\chunks.json"
EMBED_FILE = r"C:\Users\balaj\Desktop\embeddings\index.pkl"

os.makedirs(os.path.dirname(EMBED_FILE), exist_ok=True)

# Load chunks
with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Compute embeddings for each chunk
for chunk in chunks:
    # Make sure 'text' exists
    text = chunk.get("text", "")
    chunk["embedding"] = model.encode(text).tolist()

# Save embeddings
with open(EMBED_FILE, "wb") as f:
    pickle.dump(chunks, f)

print(f"Saved {len(chunks)} embeddings to {EMBED_FILE}")
