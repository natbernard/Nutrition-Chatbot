# import files
from flask import Flask, render_template, request
import os
from chat import gpt3_completion

app = Flask(__name__)
app.static_folder = 'static'

# chatbot = os.system('chat')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(gpt3_completion(userText))


if __name__ == "__main__":
    app.run()
