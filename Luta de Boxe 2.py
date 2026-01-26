import random
from time import sleep

vida_miguel = 100
vida_carolina = 100

capacidade_miguel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15 ,16, 17, 18, 19, 20]
capacidade_carolina = 67

espaco_branco = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

estado_utilizador = input("Muito bem vindo à luta da noite!! Vamos ver quem consegue sair em pé desta luta renhida!! Quando estiveres pronto para começar, escreve PRONTO!!\n\nR: ")

while estado_utilizador == "PRONTO":
    soco_miguel = random.choice(capacidade_miguel)
    soco_carolina = capacidade_carolina
    vida_miguel = vida_miguel - soco_carolina
    print(espaco_branco)
    if soco_carolina == 0:
        print(f"O Miguel continuou com {vida_miguel} de vida, a seguir à Carolina ter falhado o soco.")
    else:
        print(f"O Miguel ficou com {vida_miguel} de vida, a seguir a levar um soco da Carolina, que lhe deu {soco_carolina} de dano!!")
    sleep (2)
    if vida_miguel <= 0:
        print(f"\nO Miguel perdeu!! A Carolina continuou em pé, com {vida_carolina} de vida.")
        break
    vida_carolina = vida_carolina - soco_miguel
    print(espaco_branco)
    print(f"A Carolina ficou com {vida_carolina} de vida, a seguir a levar uma chapada de {soco_miguel} de dano!!")
    sleep(2)
    if vida_carolina <= 0:
        print(f"\nA Carolina perdeu!! O Miguel ainda está em pé, com {vida_miguel} de vida.")
        break