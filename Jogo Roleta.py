import random
numeros_possiveis = [1, 50+1]

numero_jogador = int(input("Olá!! Bem vindo ao jogo da roleta!! Quando quiseres, escreve o número que vais querer escolher!\n\nR: "))

numero_computador = random.chose(numeros_possiveis)
#numero_computador = 0

if numero_jogador == 0 and numero_computador == 0:
    print("Parabéns!! Número 0")

if numero_jogador == 