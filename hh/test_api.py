import requests

response = requests.post("http://127.0.0.1:5000/ask", json={
    "question": "What are Servoprime oils used for?"
})

print("Answer:", response.json())
