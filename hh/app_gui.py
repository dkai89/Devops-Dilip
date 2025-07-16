import streamlit as st
from pdf_loader import load_pdf, chunk_text
from gemini_helper import get_answer_from_chunks

# Load and chunk PDF once
PDF_PATH = "data/Industrial Product Line.pdf"
pdf_text = load_pdf(PDF_PATH)
chunks = chunk_text(pdf_text)

st.set_page_config(page_title="Industrial Q&A Bot", layout="wide")

st.title("🤖 Industrial Product Q&A Chatbot")

question = st.text_input("Ask your question about the product catalog:")

if question:
    with st.spinner("Thinking..."):
        answers = get_answer_from_chunks(question, chunks)
        for idx, ans in enumerate(answers, 1):
            st.markdown(f"**Answer {idx}:**\n\n{ans}\n\n---")
