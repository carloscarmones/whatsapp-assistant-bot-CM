from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "seu_token_de_verificacao"

@app.route('/')
def home():
    return 'Olá, Carlos! Seu bot está online com Flask!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge
        return 'Erro de verificação'
    return 'Webhook recebido com sucesso'

if __name__ == '__main__':
    app.run()

