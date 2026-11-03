"""
Crie um sistema que peça o usuario para digitar uma senha para acessar sua conta bancaria. Ele tem **apenas 3 tentativas** para acertar a senha.
Se ele errar as 3 tentativas, o sistema bloqueia a conta.
- A senha correta 1234
- o usuario tem 3 tentativas input();
- se errar 3 vezes, conta bloqueada
"""
#variaveis no escopo global
SENHA_CORRETA = "1234" #constante, boa pratica em python.
tentativas = 3 #uma variavel contadora, pode ser i ou j.

while tentativas > 0:
    senha = input("Digite sua senha: ") #variavel no escopo local
    if senha == SENHA_CORRETA:
        print ("acesso permitido")
        break #comando que facilita o loop
    else:
        tentativas -= 1                         #tentativas = tentativas - 1 
        print (f'senha incorreta, tentativas restantes: {tentativas}') 
    if tentativas == 0:
        print ("conta bloqueada")