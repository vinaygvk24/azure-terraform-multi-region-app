from flask import Flask
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Vinay 🚀"

@app.route('/random')
def random_string():
    return ''.join(random.choices(string.ascii_letters, k=10))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)