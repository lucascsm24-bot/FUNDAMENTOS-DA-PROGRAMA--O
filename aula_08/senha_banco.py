"""
Crie um sistema que peça o usuário para digitar uma senha para acessar sua conta bancária. Ele tem **apenas 3 tentativas** para acertar a senha.
Se ele errar as 3 tentativas, o sistema bloqueia a conta.
- A senha correta: 1234
- O usuário tem 3 tentativas input();
- Se errar 3 vezes, a conta bloqueia.
"""
# VARIÁVEIS NO ESCOPO GLOBAL
SENHA_CORRETA = "1234" # CONSTANTE, BOA PRÁTICA EM PYTHON
tentativas = 3 # UMA VARIÁVEL COMPUTADORA, PODE SER I OU J.

while tentativas > 0:
    senha = input("Digite a sua senha: ") #VARÍAVEL NO ESCOPO LOCAL
    if senha == SENHA_CORRETA:
        print(" 🔓 Senha Correta 🔓 ")
        break # COMANDO QUE FINALIZA O LOOPING
    else:
     tentativas = tentativas -1
    print(f'🔐 Senha Incorreta 🔐 Tentativas restantes:{tentativas}')
   
    if tentativas == 0:
        print("🔐 Conta Bloqueada 🔐")

