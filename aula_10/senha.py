while True:
    senha = input("🔐 Crie uma senha 🔐 (DEVE CONTER PELO MENOS 8 CARACTERES)")
    if len(senha) >= 8:
        print("🛡️ SENHA CRIADA COM SUCESSO ✅ ")
    break
else:
    print(" ❌ A SENHA PRECISA TER NO MÍNIMO 8 CARACTERS! TENTE NOVAMENTE.‼️")