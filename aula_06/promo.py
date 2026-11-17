dia = input("DIGITE O DIA DA SEMANA: ").lower()
valor = float(input("DIGITE O VALOR DO PEDIDO: "))
frete_gratis = False
if dia == "terça" and valor > 40:
    print("sobremesa grátis!")

elif dia == "quarta":
    valor = valor * 0.85
elif (dia == "sábado" or dia == "domingo") and valor > 100:
    print("FRETE GRÁTIS")
    frete_gratis = True

if not frete_gratis:
    valor = valor + 5
print(valor)