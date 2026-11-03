sabores_pizza = {"mussarela", "calabresa", "portuguesa", "frango com catupiry", "quatro queijos", "marguerita",}
print ("faça seu pedio (digite 'sair' para encerrar):")
pizza = "" #aqui ficara a armazenado o pedido do cliente

while pizza.lower() != "sair":
    pizza = input("escolha o sabor da pizza:")
    if pizza in sabores_pizza:
            print(f'{pizza} adicionado ao pizza')
    elif pizza.lower() == "sair":
        print("pedido encerrado")
    else:
        print("sabor indisponivel, escolha outro sabor")           
            
#enquato o sair nao for digitado,o while continuara sendo executado