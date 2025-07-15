# main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Carlos! Seu bot está online com Flask!"
