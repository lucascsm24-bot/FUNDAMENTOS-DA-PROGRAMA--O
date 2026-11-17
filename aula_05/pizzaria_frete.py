distancia = float(input("Digite a distância em km:"))
if distancia <= 5.00:
    print("frete: R$5,00")
elif distancia <= 10.00:
    print("frete: 10,00")
else:
    print("Não entregamos nessa distância, sinto muito")



distancia = int(input("Digite a distancia em km"))
taxa_fixa = 5.00
if distancia <= 5.00:
    valor_km = 1.00
    frete = taxa_fixa + (distancia * valor_km)
    print(f"O valor do frete é R$ {frete}")
elif distancia <= 10.00:
    valor_km = 2.00
    frete = taxa_fixa + (distancia * valor_km)
    print(f"O valor do frete é R$ {frete:.2f}")
else:
    print("Não entregamos nessa distancia.")



dia = input("Dia da semana:").lower()
valor = int(input("Valor do pedido: R$ "))
taxa_entrega = 5
mensagem_extra = ""
if dia == "terça-feira"
    if valor > 40:
    mensagem_extra(" você ganhou uma sobremesa grátis!")
elif dia == "quarta-feira":
    valor = valor - (*0.15)
    mensagem_extra("Desconto de 15% foi aplicado!")
elif (dia == "sábado") or (dia == "domingo") and valor > 100:
    taxa_entrega = 0
    mensagem_extra( "Frete grátis!")
    total = valor + taxa_entrega
    print(f"total a pagar R${valor + taxa_entrega}") + mensagem_extra

