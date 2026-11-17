# primeira funçao, calcular preço calcular_preco_pizza()

def calcular_preço_pizza(tamanho):
  tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
  "para receber o value voce acessa o key"
  return tabela.get(tamanho,0)
"tabela.ge() e uma forma segura de acessar valores no dict"
".get(tamanho,0) evita retorno NONE se a chave nao existir"


print (calcular_preço_pizza("G"))


#segunda funçao, calcular_taxa_entrega()
def calcular_taxa_entrega(distancia_km):
  if distancia_km <= 3:
    return 5.0
  elif distancia_km <=7:
    return 10.0
  else:
    return 15.0

  
  print (calcular_taxa_entrega(5))

  #terceira funçao, aplicar_desconto_fidelidade()





def aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel):
    if eh_cliente_fiel:
      return subtotal * 0.90
    return subtotal


def fecha_pedido(tamanho, ditstancia_km, eh_cliente_fidelidade):
  "Essa funçao REUTILIZA todas as funçoes anteriores"
  preço_pizza = calcular_preço_pizza(tamanho)
  taxa = calcular_taxa_entrega(ditstancia_km)
  subtotal = preço_pizza + taxa
  total = aplicar_desconto_fidelidade(subtotal, eh_cliente_fidelidade)

  print (f"Pizza ({tamanho}): R${preço_pizza:.2f}")
  print(f"Taxa de entrega: R$ {taxa:.2f}")
  print(f"Total: R$ {total:.2f}")
  print("-" * 30)
  

fecha_pedido("G", 5, True)
