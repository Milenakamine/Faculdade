#3.Exercicio da Lista Complementar - Ecila

#Escreva um programa que exiba a tabuada do número digitado,
#onde o usuário possa digitar o inicio e o fim da tabuada.

valorTabuada = int(input("Digite o numero da tabuada: "))
inicio = int(input("Digite o numero de incio da tabuada: "))
fim = int(input("Digite o número do fim da tabuada: "))
for i in range(inicio, fim + 1):
    print(f"{valorTabuada} x {i} = {valorTabuada * i}")
