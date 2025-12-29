# 🎓 Chatbot DUK Admission Assistant  

This is a Retrieval-Augmented Generation (RAG) based AI chatbot designed to assist with Digital University Kerala (DUK) 2025 admissions. It uses the official 2025 admission prospectus PDF to provide instant answers about the University, available programmes, eligibility criteria, entrance exams, fees, how to apply, and other related details. The system is built fully offline using Llama 3.2 (3B) for generation and uses `sentence-transformers/all-MiniLM-L6-v2` model for text embeddings with FAISS vector search, and implemented with a Streamlit interface.

---

## 📌 Workflow - How This Chatbot Was Built

### 1️⃣ Data Extraction & Cleaning

- The Digital University Kerala (DUK) 2025 Prospectus (30-page PDF) was first extracted because PDF format is not suitable for efficient AI retrieval.
- Text extraction was done using **Docling**, converting the PDF into a Markdown file (`duk_data.md`) for easier processing.
- After the **first cleaning cycle**, the extracted text became **933 lines** but still contains noise and broken formatting.
- To improve retrieval accuracy, only **two Markdown header levels** were used: `#` for Main sections and `##` for Sub-sections. Using only these two levels helped the retriever read the data more clearly and increased answer accuracy.
- After testing the chatbot multiple times and refining the data further, additional cleaning was performed and the final optimized dataset became **677 lines**, resulting in more reliable retrieval and better model accuracy.



