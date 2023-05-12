
#o sistema de login deve permitir que novos usuarios sejam cadastrados
# o sistema de login nao deve permitir que  usuarios duplicados sejam cadastrados
#o sistema deve alertar caso a senha e login estejam incorretos

# 1 quais sao os dados de entrada necessarios? 
# ---- usuario e senha
# 2 o que devo fazer com esses dados?
# --- devo registrar usuario e senha digitados
# 3 quais são as restrições deste sistema?
# ----o sistema não deve permitir cadastro de usuarios existentes 
# 4 qual o resultado esperado?
#---- um novo usuario e senhas cadastradas
# 5 qual a sequencia de passos necessarios?
#    - receber o usuario
#    - receber a senha
#    - verificar se existe o usuario
import pwinput

# armazenando usuarios existentes
usuarios = ["diego","eric","silvia"]
senhas = ["1234","1020","1030"]
# permitir que  usuarios existentes possam fazer  o login ( lista de usuarios). 
resposta =input("[1]- cadastrar novo usuario: [2]- fazer login: ")

if resposta == "1":
    #recebendo usuario
    newuser = input("Digite seu usuario: ")
    # o sistema não deve permitir cadastro de usuarios existentes 
    if newuser in usuarios:
        print("usuario existente")
    else:
        #recebendo uma senha
        password =pwinput.pwinput("Digite sua senha: ")
        # - caso não exista, cadastrar o usuario e senha
        usuarios.append(newuser)  
        senhas.append(password)
        print("usuario cadastrado com sucesso")
elif resposta == "2":
    # permitir que  usuarios existentes possam fazer  o login. 
    # 1º pedir usuario
    newuser = input ("Digite seu usuario: ")
    # pedir senha
    password = pwinput.pwinput("Digite sua senha: ")
    # verificar se usuario existe em uma lista de usuarios
   
        
    # for index, usuarios in enumerate(usuarios):
    if newuser in usuarios and password == senhas:
        print ("login realizado com sucesso")
        # else:
        #     print("usuario ou senha incorretos")
else:
     print("digite apenas 1 ou 2 ")           
        #2
        

            #o sistema deve alertar caso a senha e login estejam incorretos
      

