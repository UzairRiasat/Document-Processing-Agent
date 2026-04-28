# 📄 Document Processing Agent

AI-powered document processing API that converts **PDF** and **DOCX** files into structured JSON using **FastAPI**, **LangGraph**, and **OpenAI**.

Supports both:
- ☁️ OpenAI models
- 🖥️ Local LLMs with Ollama

---

# Live Demo
 https://your-app.onrender.com/docs

---

# ✨ Features

- Upload PDF or DOCX files
- Extract and structure document data into JSON
- AI-powered processing workflow using LangGraph
- Supports OpenAI and local Ollama models
- SQLite by default
- MySQL and PostgreSQL support
- FastAPI Swagger documentation included
- Ready for deployment on Render

---

# 🛠️ Tech Stack

- Python
- FastAPI
- LangGraph
- OpenAI API
- Ollama
- SQLAlchemy
- SQLite / MySQL / PostgreSQL

---

# 🚀 Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/document-processing-agent.git
cd document-processing-agent
```

---

## 2. Create Virtual Environment

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-...
DATABASE_URL=sqlite:///./doc_agent.db
```

---

## 5. Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://localhost:8000
```

---

# 📤 Upload a Document

## Swagger UI

Open:

```text
http://localhost:8000/docs
```

Use the `POST /upload` endpoint.

---

## cURL Example

```bash
curl -X POST -F "file=@your_cv.pdf" http://localhost:8000/upload
```

---

# 📚 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/upload` | POST | Upload PDF/DOCX and return structured JSON |
| `/live` | GET | Health check endpoint |

---

# 🗄️ Database Configuration

Default database:

```text
SQLite → doc_agent.db
```

---

## MySQL

```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/dbname
```

---

## PostgreSQL

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

---

# 🧠 Using Local Models with Ollama

You can run the project without an OpenAI API key.

---

## Install Ollama

Download from:

```text
https://ollama.com
```

---

## Pull a Model

```bash
ollama pull llama3.2:3b
```

---

## Remove OpenAI Key

Leave this empty in `.env`:

```env
OPENAI_API_KEY=
```

The application will automatically switch to Ollama.

---

# ☁️ Deploy on Render

## 1. Push Code to GitHub

```bash
git add .
git commit -m "Initial commit"
git push
```

---

## 2. Create a Web Service on Render

- Connect your GitHub repository
- Choose **Web Service**

---

## 3. Build Command

```bash
pip install -r requirements.txt
```

---

## 4. Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 5. Add Environment Variables

```env
OPENAI_API_KEY=your_key
DATABASE_URL=your_database_url
```

Recommended:
- Render PostgreSQL database

---

## Optional: Prevent Cold Starts

Use a free cron service like:

```text
https://cron-job.org
```

Ping:

```text
https://your-app.onrender.com/live
```

every 10 minutes.

---

# 📁 Project Structure

```text
document-processing-agent/
│
├── main.py               # FastAPI routes
├── graph.py              # LangGraph workflow
├── tools.py              # Extractor and validation tools
├── text_extractor.py     # PDF/DOCX text extraction
├── models.py             # Database models
├── config.py             # Environment configuration
├── requirements.txt      # Dependencies
├── .env                  # Environment variables
└── README.md
```

---

# 🔄 Workflow Overview

```text
Upload Document
        ↓
Text Extraction
        ↓
AI Processing (LangGraph)
        ↓
Validation & Structuring
        ↓
Structured JSON Output
```

---

# 📌 Example Response

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": [
    "Python",
    "FastAPI",
    "SQL"
  ],
  "experience": [
    {
      "company": "ABC Corp",
      "role": "Backend Developer"
    }
  ]
}
```

---

# 📄 License

This project is licensed under the MIT License.

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, open an issue first to discuss what you'd like to improve.

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.