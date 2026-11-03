# numero = int(input("🔢 Digite um número inteiro positivo para a contagem: "))

# while numero > 0:
#     print(numero)
#     # numero = numero - 1  # decrementa o número em 1 a cada iteração
#     numero -= 1
# print("🔥FOGO!!!")

# while True:
#     senha = input("🔒 Crie uma senha (deve ter no mínimo 8 caracteres): ")

#     # Verifica se o comprimento da senha é maior ou igual a 8
#     if len(senha) >= 8:
#         print("✅ Senha criada com sucesso!")
#         break  # a senha é válida, então o laço é encerrado
#     else:
#         print("❌ A senha precisa ter no mínimo 8 caracteres! Tente novamente.")

numero_secreto = 17  # o computador "pensou" este número

# Laço infinito que só será quebrado com o comando break
while True:
    palpite = int(input("Adivinhe o número secreto entre 1 e 20: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!!! ✅")
        break  # encerra o laço
    elif palpite < numero_secreto:
        print("❌ Muito baixo! Tente novamente.")
    else:
        print("❌ Muito alto! Tente novamente.")