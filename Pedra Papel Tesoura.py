# Importar bibliotecas e definir variáveis
import random
lista_pc = ["Pedra", "Papel", "Tesoura"]
opcao_pc =random.choice(lista_pc)
opcao_utilizador = input("Qual queres escolher?\n\n - Pedra\n - Papel\n - Tesoura\n\nR: ")
texto_derrota = (f"\nComo o PC escolheu {opcao_pc}, foi DERROTA do utilizador!!")

# Caso o jogo empate
if opcao_pc == opcao_utilizador:
    print(f"\nComo o PC escolheu {opcao_pc}, foi EMPATE do jogo!!")

# Caso o utilizador perca
elif opcao_pc == "Pedra" and opcao_utilizador == "Papel":
    print(texto_derrota)
elif opcao_pc == "Tesoura" and opcao_utilizador == "Papel":
    print(texto_derrota)
elif opcao_pc == "Papel" and opcao_utilizador == "Pedra":
    print(texto_derrota)

# Caso o utilizador ganhe
else:
    print(f"\nComo o PC escolheu {opcao_pc}, foi VITÓRIA do utilizador!!")