# main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return return "Bot atualizado — online com Flask!"

