# 🎓 Chatbot DUK Admission Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Llama 3.2](https://img.shields.io/badge/Model-Llama_3.2_(Ollama)-black?style=for-the-badge&logo=ollama&logoColor=white)

> **A production-grade Hybrid RAG system for Digital University Kerala (DUK) Admissions 2025. Engineered with a deterministic guardrail layer to prioritize verified admission rules over generic vector retrieval, ensuring zero hallucinations on critical queries.**

---

## 🎥 Project Demo
![Demo Preview](assets/screenshot1.png)
*(See the `assets` folder for full video demo)*

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

## 🧬 System Architecture

```mermaid
graph TD
    A[User Query] --> B{Guardrail Check}
    B -- Critical Fact Match --> C[Deterministic Answer (important_facts.md)]
    B -- No Match --> D[Vector Retrieval (FAISS)]
    D --> E[Retrieve Top-K Context Chunks]
    E --> F[Augmented Prompt (Context + History)]
    F --> G[Llama 3.2 Local Inference]
    C --> H[Streamlit UI Response]
    G --> H
