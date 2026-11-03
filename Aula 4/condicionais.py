# Estruturas condicionais permitem que o programa execute blocos de codigos diferentes dependendo de uma condição. A condição é sempre avaliada como True (verdadeiro) False(falso).


#se o ususari tiver a idade maior que 18 ele podera entrar.
# if->verifica uma condição e executa o bloco de código associado se a condição for verdadeira
#idade_usuario = 19
 # idade_usuario >18:
#   print ("o usuario pode acessar o local")

#else -> permite executar o bloco de codigo se a condiçao if for falsa

#if idade_usuario > 18:
 #   print("o usuario pode acessar o local")
#else:
 #   print("o usuario nao pode acessar o local")

#elif -> abreviaçao (else if) é usado para testar varias condiçoes.Ele so sera exibido se todas as condiçoes anteriores forem falsas.
nota = int (input("digite a nota do aluno:"))
#nota maior ou igual a 90, "aprovado com nota excelente."
#nota for maior ou igual a 70, "aprovado."
#qualquer outra nota,sera exibido "reprovado"

if nota >= 90:
    print("aprovado com nota excelente")
elif nota >= 70:
    print("aprovado")
else:
    print("reprovado")
