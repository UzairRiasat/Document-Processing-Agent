import pdfplumber
from docx import Document as DocxDocument

def extract_text_from_pdf(file_obj):
    text = []
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_text_from_docx(file_obj):
    doc = DocxDocument(file_obj)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_raw_text(file_obj, filename):
    if filename.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_obj)
    elif filename.lower().endswith(".docx"):
        return extract_text_from_docx(file_obj)
    else:
        raise ValueError("Only PDF or DOCX allowed")