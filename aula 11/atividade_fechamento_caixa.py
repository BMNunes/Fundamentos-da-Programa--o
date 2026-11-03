pizza = 0
faturamento = 0
maior_venda = 0 
menor_venda = 0
acima_50 = 0

while True:
    valor = float(input("valor da pizza vendida (0 para encerrar) R$ "))
    if valor == 0:
        break
    if valor < 0:
        print ("valor ivalido, digite um valor positivo:")
        continue
    pizza += 1
    faturamento += valor 
    if valor > maior_venda:
        maio_venda = valor
    if pizza == 1 or valor < menor_venda:
        menor_venda = valor
    if valor > 50:
        acima_50 += 1

    
    
    if pizza == 0:
        print ("nenhuma venda registrada hoje.")
    else:
        ticket_medio = faturamento / pizza
        print ("===FECHAMENTO DO CAIXA===")
        print (f"pizzas vendidas{pizza}")
        print (f"faturamento total{faturamento:.2f}")
        print (f"ticket medio{ticket_medio:.2f}")
        print (f"maior venda{maior_venda:.2f}")
        print (f"menor venda{menor_venda:.2f}")
        print (f"pizzas acima de 50 reais {acima_50}")


