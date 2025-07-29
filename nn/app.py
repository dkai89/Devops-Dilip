import streamlit as st
from rag_pipeline import query_with_gemini

st.set_page_config(page_title="Industrial RAG Bot", layout="wide")
st.title("🔍 Industrial Product RAG Assistant")

question = st.text_input("Ask a question about the industrial product line PDF:")

if st.button("Get Answer"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                answer = query_with_gemini(question)
                st.success("Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"🚨 Error: {str(e)}")
