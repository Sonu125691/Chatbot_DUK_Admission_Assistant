import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


st.markdown("""
    <style>
        /* 1. Main App Background */
        .stApp {
            background-color: #DCE4F2;
        }
        
        /* 2. Top Header */
        header[data-testid="stHeader"] {
            background-color: #DCE4F2 !important;
        }

        /* 3. Bottom Input Bar - The "Nuclear" Fix */
        div[data-testid="stBottom"] {
            background-color: #DCE4F2 !important;
        }

        /* 4. Target the inner container of the bottom bar just in case */
        div[data-testid="stBottom"] > div {
            background-color: #DCE4F2 !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓DUK Admission Assistant")
st.write("Welcome! I am Digital University Kerala(DUK) - 2025 Admission Assistant." \
         " Ask me anything about courses, fees, eligibility, entrance tests, scholarships and more.")


@st.cache_data
def load_important_facts():
    with open("important_facts.md", "r", encoding="utf-8") as file:
        return file.read()

important = load_important_facts()


@st.cache_resource
def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local("duk_faiss_index", embeddings, allow_dangerous_deserialization=True)
    return vector_db.as_retriever(search_kwargs={"k": 10})

retriever = get_retriever()


llm = OllamaLLM(model="llama3.2", temperature = 0.1, top_p = 0.9, num_ctx = 8192)

template = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an Admission Assistant for Digital University Kerala (DUK) - 2025.

RULES:
- **INTERNAL DATA SAFETY:** NEVER start your answer with "IMPORTANT FACTS:" or "RETRIEVED CONTEXT:". Do not print the provided context blocks.
- IMPORTANT FACTS are only for your internal reference. NEVER display them to the user.
- ALWAYS prioritize information under "IMPORTANT FACTS"
- Retrieved context ("RETRIEVED CONTEXT") is SECONDARY
- NEVER include disclaimers, website notes, or phrases such as 
  "the list is subject to change" or "it's best to check with the university".
- When answering, write clean, short, and structured responses.
- Only show necessary information. Do NOT repeat the user question.
- Be helpful and professional.
- Be user friendly

If the answer is not present in IMPORTANT FACTS or RETRIEVED CONTEXT, reply exactly:
"Sorry, I can't answer this question."

<|eot_id|><|start_header_id|>user<|end_header_id|>

IMPORTANT FACTS:
{important}

RETRIEVED CONTEXT:
{context}

CHAT HISTORY:
{history}

QUESTION: {question}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    prompt
    | llm
    | StrOutputParser()
)


def build_history(window_size = 3):
  recent_messages = st.session_state.messages[-(window_size * 2):]
  return "\n".join([f"{m['role'].upper()}:{m['content']}" for m in recent_messages])


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_query = st.chat_input("Ask me about Digital University of Kerala")
if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        docs = retriever.invoke(user_query)

        context_data = ""
        for d in docs:
          h1 = d.metadata.get("Header_1","")
          h2 = d.metadata.get("Header_2","")

          context_data += f"{h1} | {h2}:\n{d.page_content}\n\n"

        ai_response = rag_chain.invoke({
            "context": context_data,
            "important": important,
            "history": build_history(),
            "question": user_query
        })

        st.markdown(ai_response)

    st.session_state.messages.append({"role": "user", "content": user_query})
    st.session_state.messages.append({"role": "assistant", "content": ai_response})