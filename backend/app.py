from flask import Flask
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

# Get region from environment variable
REGION = os.getenv("REGION", "Unknown Region")

@app.route("/")
def home():
    return f"Hello from {REGION}"

@app.route("/api/random")
def random_string():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    result = ''.join(random.choice(letters) for i in range(8))
    return f"{REGION}: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
