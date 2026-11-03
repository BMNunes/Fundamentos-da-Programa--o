"""
Crie um programa que simule um caixa eletronico. o usuario pode sacar valores até que o saldo disponivel acabe ou ate ele digitar "sair".
-comece com um saldo inicial de 1500 reais 
-peça  ao usuario o valor pra saque
-se o valor for maior que o saldo, avise que nao há saldo suficiente
-se o ususario digiar "sair" enecerre o programa
"""

saldo = 500

while saldo > 0:#ira continuar ate ser False(acabar o saldo) ou digitar 'sair'
    print(f' \n saldo disponivel: {saldo: .2f}') #\n quebra a linha
    saque = input("digite o valor para sacar ou 'sair' para encerrar: ")

    if saque.lower() == "sair": #o metodo lower transforma a string em minuscula
        print ("operaçcão encerrada")
        break

    saque = float(saque)
    if saque > saldo:
        print ("saldo insuficiente")
   
    else:
     saldo -= saque
    print ("saque de {saque: .2f} realizado com sucesso")