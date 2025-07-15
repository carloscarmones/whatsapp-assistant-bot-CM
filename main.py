from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    verify_token = "seu_token_aqui"  # <<< SUBSTITUIR pelo token que você definir na Meta
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.verify_token") == verify_token:
        return request.args.get("hub.challenge")
    return "Erro de verificação", 403

@app.route('/', methods=['POST'])
def webhook():
    print(request.json)  # Teste: só mostra o corpo da mensagem recebida no log do Render
    return "Recebido", 200
