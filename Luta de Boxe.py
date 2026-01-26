# Importar bibliotecas
from random import randint
from time import sleep


# Definir vida dos jogadores
vida_jogador_a = 100
vida_jogador_b = 100


# Definir espaço branco
espaco_branco = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


# Fazer a introdução
print("\nMuito bem vindos à nossa luta da noite!! Hoje o combate será entre o Manuel e a Carolina!!")
estado_utilizador = input("\nQuando estiveres pronto para começar digita COMEÇAR!\n\nR: ")


# Condição While
while estado_utilizador == "COMEÇAR":
    soco_jogador_a = randint(0, 30)
    soco_jogador_b = randint(0, 28)
    vida_jogador_a -= soco_jogador_b
    print(espaco_branco)
    print(f"\nO Manuel ficou com {vida_jogador_a} de vida, a seguir a levar um soco de {soco_jogador_b} de dano da Carolina!!")
    sleep(2)
    if vida_jogador_a <= 0:
        print(f"\nO jogo acabou e o Manuel perdeu!! A Carolina continua em pé, com {vida_jogador_b} de vida!!")
        break
    vida_jogador_b -= soco_jogador_a
    print(espaco_branco)
    print(f"\nA Carolina ficou com {vida_jogador_b} de vida, a seguir a uma chapada do Manuel de {soco_jogador_a} de dano!!")
    sleep(2)
    if vida_jogador_b <= 0:
        print(f"\nO jogo acabou e a Carolina perdeu!! O Manuel continua em pé, com {vida_jogador_a} de vida!!")
        break