# -*- coding: utf-8 -*-

from flask import Flask, request
from embed import *
import os

app = Flask(__name__)
POST_METHOD = "POST"

@app.route('/webhook', methods=[POST_METHOD])
def webhook():
    pacotes = request.get_json()
    situacao, local , horario = []
    for codigo_pacote, informacoes in pacotes.items():
        for atualizacao in informacoes["ultimas_mudancas"]:
            situacao.append(atualizacao["situacao"])
            horario.append(atualizacao["datahora"])
            local.append(atualizacao["local"])
        em = embed(title=f"Um pacotinho mudou de status!📦🔔", color=0X6EAF2C, url=f"https://www.muambator.com.br/pacotes/{codigo_pacote}/detalhes/")
        em.footer(informacoes['nome'])
        em.desc(f"""```fix
➕ {horario[0]} {situacao[0]} \n➖ {local[0]}
        ```""")
        em.send()
    return "OK"



if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
