from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import shutil
import os

from .pipeline import add_document, answer_question

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    add_document(file_path)
    return {"message": "Document uploaded successfully"}


@app.post("/ask")
async def ask(q: str):
    answer = answer_question(q)
    return JSONResponse({"answer": answer})
