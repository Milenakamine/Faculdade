# If e Elif
categoria = int(input("Digite o categoria do produto: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("categoria inválida, digite um número de 1 a 5")

print("O preço do produto é de: R$", preco) 
