idade = int(input("Digite a sua idade para sabermos se você já pode tirar sua carteira de motorista:"))
if idade >= 18:
    print ("Parabéns!!! \nVocê já está apto para tirar sua carteira de motorista!") # o \n serve para oular linha; então o parabéns aparecerá em uma linha e o 'você está...' em outra
if idade < 18:
    print ("Você ainda não está apto para tirar sua carteira de motorista!! \nTente novamente daqui", (18-idade), "anos.")
