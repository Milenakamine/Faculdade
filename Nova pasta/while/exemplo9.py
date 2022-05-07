contador = 1
resposta = 'sim'
while (resposta == 'sim' or resposta == 's'):
    x = int(input("Digite um valor para x: "))
    r = x * 3
    print("o valor de R é: ", r)
    resposta = input("Deseja continuar? ")