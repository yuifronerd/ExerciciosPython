print ("=======Banco Central da Camix=======")
senha = int(input("Digite os numeros para sua senha: "))
while senha != 1234:
  senha = int(input("Incorreto. Digite novamente: "))
  
  if senha == 1234:
    print("Senha aceita")
