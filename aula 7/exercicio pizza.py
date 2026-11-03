dia_da_semana = input("dia da semana:").lower()
valor = float(input("digite o valor:"))
distancia = float(input("digite a distancia:"))
taxa_de_entrega = 5.00
total = valor + taxa_de_entrega
valor_por_km = 1
desconto = total * 0.15
total_com_desconto = total - desconto
frete = 5 + (distancia * valor_por_km)

if dia_da_semana == "terça" and valor > 40:
    print (f"""
        Dia da Semana:{dia_da_semana}
        valor:{valor}
        Você ganhou a sobremesa gratis!!!
        Valor Total:{total}

""")

elif dia_da_semana == "quarta":
    print (f"""
        Dia da Semana:{dia_da_semana}
        valor:{valor}
        Você ganhou 15% de desconto!!!
        Valor Total:{total_com_desconto}
        
""")

elif dia_da_semana == "sabado" or dia_da_semana == "domingo" and valor > 100:
    print (f"""
        Dia da Semana:{dia_da_semana}
        valor:{valor}
        Você ganhou frete gratis!!!
        Valor Total:{valor}
        
""")

elif dia_da_semana == "segunda" or dia_da_semana == "quinta" or dia_da_semana == "sexta":
    print (f"""
        Dia da Semana:{dia_da_semana}
        valor:{valor}
        Valor Total:{total}
        frete:{frete}
        
""")
else:
    print (f"""
        Dia da Semana:{dia_da_semana}
        valor:{valor}
        Valor Total:{total}
        frete:{frete}
        
""")
#Wa'alaikum assalam!