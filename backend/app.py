from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

@app.route('/api/health')
def health():
    return "OK", 200

@app.route("/")
def home():
    return "hi vinay"

@app.route("/api/random")
def random_string():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    result = ''.join(random.choice(letters) for i in range(8))
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)