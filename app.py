from flask import Flask, render_template, request, jsonify
from chat import gpt3_completion

app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template('index.html')

@app.post('/predict')
def predict():
    prompt =request.get_json().get('message')
    response = gpt3_completion(prompt)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug = True)
    