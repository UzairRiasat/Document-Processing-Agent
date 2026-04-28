from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Document
from text_extractor import extract_raw_text
from graph import build_graph, State
from config import DATABASE_URL

app = FastAPI(title="Document Processing Agent")

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
graph = build_graph()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
        raise HTTPException(400, "Only PDF or DOCX files allowed")
    
    try:
        raw_text = extract_raw_text(file.file, file.filename)
    except Exception as e:
        raise HTTPException(500, f"Text extraction failed: {str(e)}")
    
    state = State(
        raw_text=raw_text,
        extracted={},
        missing_fields=[],
        iterations=0,
        max_iterations=3,
        final_output=None
    )
    
    final_state = graph.invoke(state)
    
    db = SessionLocal()
    doc = Document(
        filename=file.filename,
        raw_text=raw_text[:5000],
        extracted_data=final_state["final_output"]
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    db.close()
    
    return {
        "id": doc.id,
        "extracted_data": final_state["final_output"],
        "missing_fields": final_state["missing_fields"]
    }

@app.get("/")

@app.get("/live")
async def live_check():
    return {"status": "alive"}


def root():
    return {"message": "Document Processing Agent is running. POST /upload"}