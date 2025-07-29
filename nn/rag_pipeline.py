import asyncio
import sys

# ✅ Windows asyncio fix
if sys.platform.startswith('win') and sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from pdf_parser import extract_pdf_text
from utils import split_text_into_chunks
import google.generativeai as genai

# ✅ Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

PDF_PATH = "data/Industrial Product Line.pdf"
INDEX_PATH = "index/vector_index"

# ✅ Build vector store
def build_vector_store():
    text = extract_pdf_text(PDF_PATH)
    chunks = split_text_into_chunks(text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.from_documents(docs, embedding)
    db.save_local(INDEX_PATH)

# ✅ Async Gemini Query
async def query_with_gemini_async(query):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.load_local(INDEX_PATH, embedding, allow_dangerous_deserialization=True)

    results = db.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in results])

    model = genai.GenerativeModel("models/gemini-pro")  # ✅ This now works after SDK upgrade
    response = await model.generate_content_async(f"""
        You are a helpful assistant. Use the following extracted document to answer the user's question.

        Context:
        {context}

        Question:
        {query}
    """)
    return response.text

# ✅ Streamlit wrapper
def query_with_gemini(query):
    return asyncio.run(query_with_gemini_async(query))
