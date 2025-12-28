# 🎓 Chatbot DUK Admission Assistant  
AI-Powered RAG Chatbot for Digital University Kerala (DUK) – 2025 Admissions

This project is a **local RAG-based chatbot** built using **Llama 3.2 (3B local model)**, **FAISS vector search**, and **Streamlit UI**.  
It intelligently answers questions about **Digital University Kerala (DUK) Admission 2025** including eligibility, courses, fees, entrance exam details, scholarships, & more.

---

## 🚀 Project Highlights

- 🔥 Built a complete **Retrieval-Augmented Generation (RAG)** pipeline
- 🧠 **30-page DUK Prospectus → Converted → Cleaned → Reduced → Knowledge Base (677 lines)**
- 🧩 Used intelligent chunking:
  - `MarkdownHeaderTextSplitter` → 29 initial chunks
  - `RecursiveCharacterTextSplitter` (250 len + overlap 60) → 43 optimized chunks
- 🏦 Vector Store: **FAISS** (locally stored, `.load_local`)
- 🤖 Model: **Llama 3.2 – 3B** (via Ollama) – runs **fully offline**
- 🎯 Hallucination handled using **Important Facts RL-style improvement loop**
  - First run gave hallucinations → user added curated facts file → improved accuracy significantly
- 💻 UI made using **Streamlit** with custom theme & clean UX

---

## 🧱 Architecture (RAG Pipeline)

```mermaid
flowchart TD
    A[PDF Prospectus 2025] --> B[docling extract → duk_data.md]
    B --> C[Clean & Reduce to 677 lines]
    C --> D[Chunking → 29 header chunks]
    D --> E[Recursive Splitter → 43 final chunks]
    E --> F[HuggingFace Embeddings all-MiniLM-L6-v2]
    F --> G[FAISS Vector Store]
    G --> H[Retriever (k=10)]
    H --> I[Prompt Template + Important Facts]
    I --> J[Llama 3.2 (Ollama)]
    J --> K[Streamlit Chat UI]

