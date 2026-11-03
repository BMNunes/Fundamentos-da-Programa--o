#perguntas a serem feitas ao cliente
#pizza pequena =19,90
#pizza media =29,90
#pizza grande =39,90
#comprando qualquer pizza e qualquer tamanho no sabado, o refri e gratuito 
Frete = 2
dia_da_semana = "quarta"

print(f"""

        =================================
        Seja Bem Vindo a pizzaria sabores
        =================================

""")
nome_cliente = input(f"""
    Digite seu nome:
""")
pizza_sabor = input("""
        Escolha uma das opçcoes abaixo:
        1-Para frango com requeijao
        2-Para calabresa
        3-Mussarela
        4-banana com chocolate
    """)
pizza_tamanho = input(f"""
        Escolha o tamanho da pizza:
        1-pequena
        2-media
        3-grande

""")
forma_entrega = input("""

        Escolha a forma de entrega:
        1-consumo no local
        2-entrega na residencia

""")

#estrutura condicional para promoçao:
#comprando qualquer pizza e qualquer tamanho no sabado, o refri é gratuito
#comprando uma pizza calabresa tamanho medio, em qualquer dia, o frete e gratuito.
#comprando qualquer pizza de qualquer tamanho no domingo,o frete e o refri sao gratuitos
if dia_da_semana == "sabado":
    print(f"pedido aceito com sucesso!")
    print(f"o refri hoje e por conta da casa")
elif dia_da_semana == "domingo":
     print(f"pedido aceito com sucesso!")
     print(f"o frete e o refri hoje e por conta da casa")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
     print("A pizza sai de graça")

# print(f"""
#         =====================================
#                RESUMO DO PEDIDO
#             Nome do cliente: {nome_cliente}
#             Sabor da pizza: {pizza_sabor}
#             Tamanho da pizza: {pizza_tamanho}
#             forma de entrega: {forma_entrega}
#         =====================================
# """)