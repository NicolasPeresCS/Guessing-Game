import random
from random import randint

loop = True
while loop:
    EscolhaComputador = randint(1, 10)
    Escolhahumana = None

    acertou = True
    print("estou pensando em um numero de 1 a 10, você consegue adivinhar qual é? ")
    while acertou:
        Escolhahumana = int(input(""))
        
        if Escolhahumana > EscolhaComputador:
            print("errou... é um numero menor, tente de novo")
        elif Escolhahumana < EscolhaComputador:
            print("errou, é um numero maior, tente de novo")
        elif Escolhahumana == EscolhaComputador:
            correto = str(input("você acertou, deseja tentar outra vez com outro numero? s/n "))
            if correto == ("s"):
                acertou = False
            elif correto == ("n"):
                loop = False
                acertou = False

                

            


