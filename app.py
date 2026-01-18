import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# It will look for the GROQ_API_KEY you set in Render
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": data['message']}]
        )
        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
