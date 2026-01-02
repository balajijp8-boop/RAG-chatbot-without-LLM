import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

EMBED_FILE = r"C:\Users\balaj\Desktop\embeddings\index.pkl"

with open(EMBED_FILE, "rb") as f:
    chunks_with_embeddings = pickle.load(f)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query):
    query_emb = embed_model.encode(query)
    sims = [cosine_similarity([query_emb], [chunk["embedding"]])[0][0] for chunk in chunks_with_embeddings]
    best_idx = sims.index(max(sims))
    return chunks_with_embeddings[best_idx]["text"]
