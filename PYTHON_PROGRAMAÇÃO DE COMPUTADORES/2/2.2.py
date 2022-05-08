# condição if e else
minutos = int(input("Quantos minutos foram utilizados no mês: "))

if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print("O valor a ser pago esse mês é de R$:", minutos*preço) 
