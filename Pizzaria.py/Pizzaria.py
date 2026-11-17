# Pergunta a serem feias ao cliente.
frete = 2
dia_semana = "sábado"  
# pizza pequena = 19,90
# pizza média = 29,90
# pizza grande = 39,90
# comprando qualquer pizza, e, qualquer tamanho no sábado, o refrigerante é gratuito.
print(f"""
     =====================================
        Seja bem vindo a pizzaria Sabores 
     =====================================
""")

nome_cliente = input(f""" 
                Digite seu nome:
""")
pizza_sabor = input(f"""
    Escolha uma das opções abaixo:
    Pizzas dispníveis: 
    1- frango com requeijão
    2- para calabresa
    3- mussarela
    4- banana com chocolate
    """)
pizza_tamanho = input("""
        ESCOLHA O TAMANHO DA PIZZA:
            1- pequueno
            2- médio
            3- grande
""")
forma_entrega = input("""
        🏍️ escolha a forma de consumação:
            1- consumo no local
            2- entrega a domicílio        
""")

# Estrutura condicional para a promoção: 
# Comprando qualquer pizza, de qualquer tamanhp, no sábado, o refrigerante sai de graça.
# Comprando uma pizza de calabresa de tamanho médio, qualquer dia, o frete é gratuito.
# Comprando qualquer pizza de qualquer tamanho no DOMINGO, o frete e o refrigerante são gratuitos.

if dia_semana == "sábado": 
    print("Pedido aceito com sucesso")
    print("O refrigerante hoje, é por conta da casa :)")
elif dia_semana == "domingo":
     print("Pedido aceito com sucesso")
     print("O frete e o refri, são por conta da casa")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media" :
    print(F" Pedido aceito com sucesso")
    print(F" O frete hoje é por conta da casa")


# print(f"""
#     =====================================
#             RESUMO DO PEDIDO
#         NOME DO CLIENTE:{nome_cliente}
#         SABOR DA PIZZA: {pizza_sabor}
#         TAMANHO DA PIZZA: {pizza_tamanho}
#         FORMA DE ENTREGA: {forma_entrega}
#     ======================================

#     """)