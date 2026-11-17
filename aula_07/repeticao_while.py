sabores_pizza = ["Mussarela", "Calabresa", "Quatro queijos", "Peperone", "Frango com catupiry", "Portuguesa"]
print("Faça seu pedido (digite 'sair' para encerrar): ")
pizza = "" #AQUI VAI FICAR ARMAZENADO A PIZZA DO CLIENTE

#ENQUANTO O "SAIR" NÃO FOR DIGITADO, O WHILE CONTINUARÁ SENDO REPETIDO.
while pizza.capitalize() != "Sair":
    pizza = input("Escolha um sabor: ").capitalize()
    if pizza in sabores_pizza:
        print(f'{pizza} foi adicionado ao seu carrinho.')
    elif pizza.capitalize() == "Sair":
        print("pedido encerrado")
    else: 
        print("Não temos este sabor no momento em nosso cardápio. Escolha outro:")
