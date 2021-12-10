from CurrencyConversion import get_currency_quote

with open("precos.csv", "r") as arquivo:
    lista_precos = arquivo.read().split("\n")

for linha in lista_precos:
    mercadoria, valor, moeda = linha.split(",")
    cotacao = get_currency_quote(moeda, "BRL")
    print(f"{mercadoria} costs R${float(cotacao) * float(valor):,.2f} today")