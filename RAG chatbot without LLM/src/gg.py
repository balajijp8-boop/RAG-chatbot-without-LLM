import pickle

with open(r"C:\Users\balaj\Desktop\embeddings\index.pkl", "rb") as f:
    data = pickle.load(f)

print(type(data))
print(len(data))
print(data[:2])  # print first 2 items to see structure
