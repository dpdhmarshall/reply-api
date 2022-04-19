from flask import Flask, jsonify 
import random

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return "<p>api running</p>"
    
# Used to show working API
@app.route('/hello')
def reply():
    return jsonify({"Reply" : "Hello there, stranger!"})

# Used for Prometheus scraping and display/alerts for Grafana dash
@app.route('/datagen')
def generate():
    return jsonify({"data" : random.randint(0, 10000)})


if __name__ == '__main__':
    app.run()