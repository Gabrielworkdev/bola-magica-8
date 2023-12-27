while True:
    username = input("Digite seu nome:")

    if username != "Gabriel":
        print("Nunca nem vi")
        break 
    senha = input("Qual a sua senha?")
    if senha == "1234":
        print("Bem-vindo, {}".format(username))
        print("Aceita um café?")
        
        break