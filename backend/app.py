from flask import Flask
import random
import string

app = Flask(__name__)
CORS(app)  # allow calls from your frontend

@app.route('/')
def home():
    return "Hello Vinay 🚀"

@app.route("/api/random")
def random_string():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(letters) for i in range(8))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)