from flask import Flask, render_template, request, jsonify
from chat import gpt3_completion, open_file

app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template('index.html')

@app.post('/predict')
def predict():
    conversation = list()
    print('NAWI: Hi there! How may I help you today?')
    while True:
        user_input = request.get_json().get('message')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '\nNAWI:'
        response = gpt3_completion(prompt)
        message = {"answer": response}
        conversation.append('NAWI: %s' % response)
        return jsonify(message)

if __name__ == '__main__':
    app.run(debug = True)
    