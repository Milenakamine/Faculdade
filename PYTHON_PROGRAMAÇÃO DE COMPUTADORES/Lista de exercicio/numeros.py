soma = 0
quantidade = 0
while True:
    number = int(input("Digite o número desejado: "))
    if number == 0:
        break
    soma = soma + number
    quantidade = quantidade + 1
print("Foram digitados:", quantidade, "números.")
print("A soma dos números é igual a: ",soma)
print(f"A sua média é de:{soma/quantidade:10.2f}")
