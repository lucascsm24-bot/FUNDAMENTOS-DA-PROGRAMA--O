# Estruturas condicionais permiem que o programa execute bloco de código diferenes dependendo de uma condição. A condição é sempre avaliada como True(verdadeiro) e False(falso). 

# if -> Verifica uma condição e executa o bloco de código associado se a condição for verdadeira.
# Se o usuário tiver a idade maor de 18, ele poderá entrar.
idade_usuario = 20 # Hardcode
# if idade_usuario > 18: 
#     print("O usario pode acessar o local.")

# else -> Permite executar o bloco de código se a condição if for falsa.
# if idade_usuario > 18: 
#     print("👍O  usuário pode acessar o local.")
# else: 
#     print("Usuáro proíbido! 🚷")

# elif -> Abreviação (else if) é usado para testar várias condições. Ele só será exibido se todas as condições anteriores forem falsas.
nota = input ("digite a nota do aluno")
# nota maior ou igual a 90, "APROVADO COM EXCELÊNCIA!"
# nota for maior ou igual a 70, "APROVADO!"
# qualquer outra nota, será exibido "REPROVADO!"

if nota >= 90:
    print("APROVADO COM EXCELÊNCIA!")  
elif nota >= 70: 
    print("APROVADO!")
else:
    print("REPROVADO!") 