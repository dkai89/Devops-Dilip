# test_requirements.py
required_modules = [
    "streamlit",
    "PyPDF2",
    "langchain",
    "chromadb",
    "google.generativeai",
    "tqdm",
    "faiss",
    "dotenv"
]

failed = []

for module in required_modules:
    try:
        __import__(module.split('.')[0])
        print(f"✅ {module} is installed.")
    except ImportError:
        print(f"❌ {module} is NOT installed.")
        failed.append(module)

if not failed:
    print("\n🎉 All requirements are installed.")
else:
    print("\n⚠️ Missing modules:", failed)
