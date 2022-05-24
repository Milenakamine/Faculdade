#Podemos realizar cálculos também, apenas armazenar os número da maneira certa
print("A função que você está prestes a realizar segue o formato de: a+b*c; defina um valor para a, b e c")
a = int(input("Digite o valor de 'a': ")) #aqui eu armazeno os valores nas variaveis para depois chama-las
b = int(input("Digite o valor de 'b':")) #outro ponto que deve ser considerado é: tudo o que se recebe no input é string, então precisamos informar o programa que vamos receber um número
c = int(input ("Digite o valor de 'c':")) #um inteiro (int) ou um float, para o programa ler em número
conta = a+b*c #aqui é onde eu armazeno na variavel conta, a conta que deve ser feita pelo programa
print ("O resultado da sua conta é:", conta) #Aqui eu apresento o valor da conta, onde eu apenas coloca um print e a variavel conta onde esta armazenado todos os valores que eu desejo
