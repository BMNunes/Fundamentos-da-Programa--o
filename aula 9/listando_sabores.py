# # sabores = ["Mussarela", "Calabresa", "Pepperoni", "Quatro Queijos", "carne", "queijo", "flango"]
# # sabores_especiais = ["Frango com Catupiry", "Portuguesa", "Marguerita", "Napolitana"]

# # print("Sabores disponíveis na Pizzaria Sabores:")
# # for sabor in sabores:
# #     # print(f"{sabor}")
# #     print(sabor)
# print ("preparando sua pizza:")
# for minuto in range(1, 6):
#     print(f"minuto {minuto} se passaram")

# print("pizza pronta, bom apetite!")

clientes = ["joão", "maria", "carlos", "ana", "pedro"]

print("atendendo clientes:")
for i, cliente in enumerate(clientes):
    if i == 3:
        print("capacidade maxima atendida, nao podemos tender mais clientes agora")
        break
    print(f"atendendo cliente {cliente}...")