from CurrencyConversion import get_currency_quote


# LER ARQUIVO DE PREÇOS
with open("precos.csv", "r") as arquivo:
    lista_precos = arquivo.read().split("\n")
    
    
# LOOP DE LEITURA DA INFORMAÇÃO DO ARQUIVO (linha à linha)
for linha in lista_precos:
    mercadoria, valor, moeda = linha.split(",")
    cotacao = get_currency_quote(moeda, "BRL")
    print(f"{mercadoria} costs R${float(cotacao) * float(valor):,.2f} today")
