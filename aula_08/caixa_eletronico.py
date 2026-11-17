"""
Crie um programa que simule um caixa eletrônico. O usuário pode sacar valores até que o saldo disponível acabe ou até ele digitar "sair".
- Comece com o saldo inicial de $500.
- Peça ao usuário digitar o valor de SAQUE:
- Se o valor for maior que o saldo, avise que o saldo é insuficiente.
- Se o usuário digitar "SAIR" encerre o programa.
"""
saldo = 500

while saldo > 0: # Irá continuar até ser False (ACABAR O SALDO) ou digitar "sair"
    print(f'\n 💵💰 Saldo disponível R${saldo:.2f}') # \N QUEBRA A LINHA
    saque = input("Digite o valor para sacar ou 'sair' para encerrar: ")

    if saque.lower() == "sair": # LOWER() TRANSFORMA A STRING EM MINÚSCULA.
        print("🏧 Operação Encerrada 🛡️")
        break
    
    saque = float(saque)
    if saque > saldo:
        print("Saldo Insuficiente! ❌")
    else:
        # SALDO = SALDO - SAQUE
        saldo -= saque
        print(f'Saque de R${saque:.2f} realizado com sucesso!')