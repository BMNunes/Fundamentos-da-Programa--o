# distancia = float(input(f"""

#         ---------------------------------
#              digite sua distancia
#         ---------------------------------


# """))
# if distancia <= 5:
#     print ("o valor da sua entrega serà 5 reais")
# elif distancia <=10:
#     print("o valor da sua entrega será 10 reais")
# else:
#     print("desculpe não entregamos")

# distancia = float(input("digite sua distancia:"))
# valor_km = 1
# frete = 5+distancia*valor_km

# if distancia <=5:
#     print (f"valor do frete {frete}")
# elif distancia <=10:
#     print (f"valor do frete {frete}")
# else:
#     print("desculpe nao entregamos")

dia = input("dia da semana:").lower()
valor = float(input("valor do pedido:"))
frete = 5

if dia =="terça" and valor >= 40:
    print ("você recebera a sobremesa por conta da casa!")
else:
    print("TMNC")