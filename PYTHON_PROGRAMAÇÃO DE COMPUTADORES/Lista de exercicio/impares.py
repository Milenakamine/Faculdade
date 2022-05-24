#2.Exercicio da Lista Complementar - Ecila

#Escreva um programa que mostre os números de 1
#até um numero digitado pelo usuário, mas, apenas os números impares.

numero = int(input('Digite o número desejado: ')) #armazena o valor que será dado pelo usuário
x = 1 #variavel
while x <= numero: 
	while x % 2 != 0: #a validação para saber se p número é par ou impar
                          #o numero inserido precisa ser diferente de 0 quando ocorre a divisão do mesmo por 2
		print(x) #quando o numero inserido não der 0 na divisao por 2 mostrará na tela
		x = x + 1	
	x = x + 1


