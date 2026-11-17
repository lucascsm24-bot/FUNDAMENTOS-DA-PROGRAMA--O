# Priemira função que calcula o preço_pizza()

def calcular_preco_pizza(tamanho):
      tabela = {"P": 25.0, "M": 35.0, "G": 45.0,}
      #PARA ACESSAR O VALOR DA PIZZA, BASTA CHAMAR A FUNÇÃO E PASSAR O TAMANHO COMO ARGUMENTO
      return tabela.get(tamanho, 0.0)  # Tabela é uma forma segura de acessar os valores. Retorna 0.0 se o tamanho não estiver na tabela


def calcular_taxa_entrega(distancia_km):
    if distancia_km <= 3:
        return 5.0
    elif distancia_km <= 7:
        return 10.0
    else:
        return 15.0

print(calcular_taxa_entrega(5))  # Testando uma distância menor ou igual a 7 km, deve retornar 10.0
# Terceira função que calcula o preço total do pedido, incluindo o preço da pizza e a taxa de entrega

def calcular_preco_total(subtotal, eh_cliente_fiel ):
   if eh_cliente_fiel:
    return  subtotal * 0.90  # Aplica um desconto de 10% para clientes fiéis
   return subtotal  # Retorna o subtotal sem desconto para clientes não fiéis      


def fechar_pedido(tamanho, distancia_km, eh_cliente_fiel): # Essa função reutiliza todas as funçõoes anteriores para calcular o preço total do pedido
    preco_pizza = calcular_preco_pizza(tamanho)
    taxa_entrega = calcular_taxa_entrega(distancia_km)
    subtotal = preco_pizza + taxa_entrega
    preco_total = calcular_preco_total(subtotal, eh_cliente_fiel)

    print(f"Pizza ({tamanho}): R$ {preco_pizza:.2f}")
    print(f"Taxa de entrega: R$ {taxa_entrega:.2f}")
    print(f"Total: R$ {preco_total:.2f}")
    print("-" * 30)

fechar_pedido("G", 5, True)