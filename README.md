# 🚗 AutoCompliance AI

An AI-powered assistant for automotive engineers to understand and query **ISO 26262** and **ASPICE** concepts using a **local LLM + RAG pipeline**.

---

## 🔥 Features

* 🧠 Local LLM (runs via Ollama – no API cost)
* 📚 Retrieval-Augmented Generation (RAG)
* 📄 Answers based on your own ISO/ASPICE documents
* 🧾 Structured responses
* ⚡ FastAPI backend for real-world usage
* 💾 Persistent vector database (Chroma)

---

## 🏗️ Architecture

User Query
→ Retrieve relevant documents (Chroma DB)
→ Inject context into prompt
→ Local LLM (Ollama)
→ Structured response

---

## 🛠️ Tech Stack

* Python
* Ollama (local LLM)
* LangChain
* ChromaDB
* FastAPI

---

## 📁 Project Structure

```
app/
  ├── main.py        # FastAPI backend
  ├── chatbot.py     # CLI chatbot
  ├── prompts.py     # system prompts
  ├── rag.py         # RAG pipeline

data/                # ISO & ASPICE text data
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/your-username/auto-compliance-ai.git
cd auto-compliance-ai
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Ollama

Make sure Ollama is installed and run:

```
ollama run phi3
```

---

### 5. Run the API

```
uvicorn app.main:app --reload
```

Open:
👉 http://127.0.0.1:8000/docs

---

## 🧪 Example Query

```
What is ASIL?
```

### Sample Output

```json
{
  "concept": "ASIL",
  "explanation": "Automotive Safety Integrity Level...",
  "example": "Used in braking systems",
}
```

---

## 🚀 Future Improvements

* Hybrid search (keyword + semantic)
* Better ranking for SWE processes
* UI dashboard
* Multi-turn conversational memory

---

## 💬 Author

Built as part of an AI engineering transition journey.
