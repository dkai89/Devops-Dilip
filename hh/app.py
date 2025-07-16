from flask import Flask, request, jsonify
from pdf_loader import load_pdf, chunk_text
from gemini_helper import get_answer_from_chunks

app = Flask(__name__)

PDF_PATH = "data/Industrial Product Line.pdf"
pdf_text = load_pdf(PDF_PATH)
chunks = chunk_text(pdf_text)

@app.route("/")
def home():
    return "Industrial Q&A Bot is running!"

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Question is required"}), 400
    answers = get_answer_from_chunks(question, chunks)
    return jsonify({"answers": answers})

if __name__ == "__main__":
    app.run(debug=True)
