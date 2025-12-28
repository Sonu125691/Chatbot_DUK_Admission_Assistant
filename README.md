# 🎓 Chatbot DUK Admission Assistant


**A production-grade Hybrid RAG system for Digital University Kerala (DUK) Admissions 2025. Engineered with a deterministic guardrail layer to prioritize verified admission rules over generic vector retrieval, ensuring zero hallucinations on critical queries.**

---

## 🚀 The Engineering Challenge
University admission data is high-stakes. A standard "probabilistic" LLM might hallucinate a degree that doesn't exist, leading to misinformation. 

**The Problem:**
* **Hallucinations:** Generic RAG models often invent answers when data is ambiguous.
* **Unstructured Data:** The 2025 Prospectus was a complex PDF, making standard retrieval noisy.
* **Latency:** Cloud models are slow and expensive for simple queries.

**My Solution: The Hybrid RAG Architecture**
I engineered a system that balances **Vector Retrieval** with **Hard Logic**:
1.  **Deterministic Guardrails (Layer 1):** A strict `important_facts.md` injection layer handles binary facts (e.g., "Do you offer B.Tech?"). This overrides the LLM to ensure **0% hallucination** on critical exclusion criteria.
2.  **Semantic Search (Layer 2):** Uses **FAISS** + **HuggingFace Embeddings** (`all-MiniLM-L6-v2`) to retrieve context for open-ended queries (e.g., "Explain the MSc Ecology syllabus").
3.  **Local Inference:** Powered by **Llama 3.2 (3B)** running locally via Ollama for privacy and speed.

---

## 🛠️ Technical Stack

* **LLM:** Llama 3.2 (3B Parameters) via Ollama.
* **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2` (Optimized for CPU latency).
* **Vector DB:** FAISS (Local flat index).
* **Orchestration:** LangChain.
* **Frontend:** Streamlit with custom CSS injection for a seamless UI.

---

## 🎥 Project Demo

![Demo Preview](assets/screenshot1.png)
