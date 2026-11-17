pizzas = 0
faturamento = 0
maior_venda = 0
menor_venda = 0
acima_50 = 0 

while True:
    valor = float(input("Valor da pizza vendida 🍕(0 para encerrar) R$:"))
    if valor == 0:
        break
    if valor < 0:
        print("⚠️ VALOR INVÁLIDO! Digite um valor positivo: ")
        continue
    pizzas += 1
    faturamento += valor
   
    if valor > maior_venda: #NA PRIMEIRA VENDA, ELE(VALOR), É MAIOR 
        maior_venda = valor
    if pizzas == 1 or valor < menor_venda:
        menor_venda = valor
    if valor > 50:
        acima_50 += 1

if pizzas == 0:
        print("❌ Nenhuma venda registrada hoje ❌ ")
else:
    ticket_medio = faturamento / pizzas
    print("=== FECHAMENTO DO CAIXA ===")
    print(f"pizzas vendidas: {pizzas}")
    print(f" Faturamento total: R$ {faturamento.2f}")
    print(f" Ticket Medio: R$ {ticket_medio.2f}")
    print(f" Maior Venda: R$ {maior_venda.2f}")
    print(f" Menor Venda: R$ {menor_venda.2f}")
    print(f" Pizzas acima de R$50.00 {acima_50.2f}")
   