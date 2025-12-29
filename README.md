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
 
### 2️⃣ Hybrid Chunking & Embedding Preparation

- A hybrid chunking strategy was used to prepare the text for retrieval.
  - First, the cleaned Markdown file was split using `MarkdownHeaderTextSplitter`, based on the `#` and `##` headings. This produced 29 structured chunks.
  - After that, a second split was done using `RecursiveCharacterTextSplitter` with a chunk size of 250 tokens and a 60-token overlap. This produced 43 final text chunks.
  - The 250-token size was chosen intentionally because the embedding model can process approximately 256 tokens, so staying within 250 prevents loss of information.
- For embedding generation, the model `sentence-transformers/all-MiniLM-L6-v2` was used.
  - This model converts text into 384-dimensional embeddings.
- Once the embeddings were generated, they were saved into a FAISS vector database.

### 3️⃣ Important Facts File (Manual Accuracy Reinforcement)

- During testing, the chatbot sometimes generated wrong or incomplete answers. To solve this, an additional file named `important_facts.md` was created.
- This file contains the most important factual points that the model must follow while answering.
- Whenever the chatbot responded incorrectly during testing, the correct factual information was identified and added into this file.
- This process made the model more accurate, because the retrieval context is checked only after referring to the information inside `important_facts.md`, giving it the highest priority.

### 4️⃣ Application Logic

- The chatbot interface was built using **Streamlit**, providing a simple and interactive chat UI.
- The RAG model runs **fully offline** using **Ollama** with the **Llama 3.2 (3B)** model.
  - This model was selected because it fits and performs efficiently on my laptop with an **RTX 4050 (6GB VRAM)**.
- The FAISS index (`duk_faiss_index`) is loaded inside the app, and retriever is created to fetch the most relevant chunks based on user questions.
  - The retriever uses **k = 10**, which was chosen because returning 10 top chunks resulted in the most accurate answers during testing.
- The file `important_facts.md` is loaded first and always given highest priority inside the prompt. Retrieved context from FAISS is only considered after that.
- A **custom system prompt** was engineered to:
  - block hallucinations
  - avoid printing internal context
  - force clean and structured answers
  - reply only when information exists
  - if information is missing, the model must reply **exactly**: `"Sorry, I can't answer this question."`
- A small chat history window was implemented with a **window size of 3 messages**.  
  - This design intentionally limits past context to avoid unnecessary prompt expansion, which reduces hallucination risk and preserves clean output.
- Hyperparameters tuned for stability and accuracy:
  - The temperature is set to **0.1** to keep responses factual. 
  - The top_p value is set to **0.9** to prevent random or creative answers. 
  - The num_ctx value is set to **8192** because this is the maximum context window of Llama 3.2 (3B), allowing long prompts to be processed without truncation.

---

## 🎥 Demo

👉 Watch the video demonstration of the chatbot here:  
🔗 [Demo Video – DUK Admission Assistant](VIDEO_LINK_HERE)







