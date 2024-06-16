from tkinter import *
import requests
from datetime import datetime
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y, Horário de Brasília: %H:%M")

## Créditos: Hastag Programação.
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: R$ {cotacao_dolar}
    Euro: R$ {cotacao_euro}
    BTC: R$ {cotacao_btc}'''

    texto_cota["text"] = texto
    texto_info["text"] = (f"Cotações da data: {data_e_hora_sao_paulo_em_texto}.")
    botao["text"] = "Cotação fornecida com sucesso!" 




janela = Tk()
janela.title("Cotação Dolar Euro e BTC para Reais")

texto_info = Label(janela, text="Clique no botão abaixo para ver as cotações das moedas atualizadas")
texto_info.grid(column=0, row=0)

espaco = Label(janela, text=" ")
espaco.grid(column=0, row=1)

botao = Button(janela, text="Buscar cotações atualizadas", command=pegar_cotacoes)
botao.grid(column=0, row=2)

texto_cota = Label(janela, text=" ")
texto_cota.grid(column=0, row=3)


janela.mainloop()