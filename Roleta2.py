import time
from random import randint
saldo = 100

try:
    def roleta(saldo):
        print(f"\nTens {saldo}$ de saldo!!")
        valor_apostado = float(input("\nQual é o valor que queres apostar?\n\nR: "))
        while valor_apostado > saldo or valor_apostado == 0:
            valor_apostado = float(input("\nAhh seu malandro, tu sabes o que fizeste, aposta outro valor!!\n\nR: "))
        while valor_apostado == saldo:
            apostar_saldo = int(input("\nTens a certeza de que queres apostar o teu saldo todo??\n\n - Sim (1)\n - Não (2)\n\nR: "))
            if apostar_saldo == 2:
                valor_apostado = float(input("\nQual é o valor que queres apostar?\n\nR: "))
            else:
                break
        jogo_roleta = int(input("\nQual é o jogo que queres escolher?\n\n - Maior ou inferior (1)\n - Vermelho ou Preto (2)\n - Número exato (3)\n\nR: "))
        while jogo_roleta != 1 and jogo_roleta != 2 and jogo_roleta != 3:
            jogo_roleta = int(input("\nModo de jogo inválido! Qual é o jogo que pretendes jogar?\n\n - Acima ou abaixo (1)\n - Vermelho ou Preto (2)\n - Número exato (3)\n\nR: "))
        saldo -= valor_apostado
        numero_sorteado = randint(0, 50 + 1)
        if jogo_roleta == 1:
            acima_ou_abaixo = int(input("\nPretendes apostar que o número que calha é acima ou abaixo de 25?\n\n - Acima (1)\n - Abaixo (2)\n\nR: "))
            if numero_sorteado >= 25:
                if acima_ou_abaixo == 1:
                    valor_ganho = valor_apostado + valor_apostado * 0.5
                    saldo += valor_ganho
                    print(f"\nBoa!! Calhou acima de 25, pois saiu o número {numero_sorteado}!! Ganhaste {valor_ganho}$, e ficaste com {saldo}$ de saldo.")
                elif acima_ou_abaixo == 2:
                    print(f"\nEpahh perdeste, que pena. O número que calhou foi {numero_sorteado}, e apostaste que era abaixo de 25!! \n\nO teu saldo ficou em {saldo}$.")
            if numero_sorteado < 25:
                if acima_ou_abaixo == 1:
                    print(f"\nEpahh perdeste, que pena. O número que calhou foi {numero_sorteado}, e apostaste que era cima ou igual a 25!! \n\nO teu saldo ficou em {saldo}$.")
                elif acima_ou_abaixo == 2:
                    valor_ganho = valor_apostado + valor_apostado * 0.5
                    saldo += valor_ganho
                    print(f"\nBoa!! Calhou abaixo de 25!! Ganhaste {valor_ganho}$, e ficaste com {saldo}$ de saldo.")
        if jogo_roleta == 2:
            vermelho_ou_preto = int(input("\nPretendes apostar que o número que calha é vermelho ou preto?\n\n - Vermelho (1)\n - Preto (2)\n\nR: "))
            if numero_sorteado % 2 == 0:
                if vermelho_ou_preto == 1:
                    valor_ganho = valor_apostado + valor_apostado * 0.5
                    saldo += valor_ganho
                    print(f"\nBoa!! Calhou um número vermelho!! Ganhaste {valor_ganho}$, e ficaste com {saldo}$ de saldo.")
                elif vermelho_ou_preto == 2:
                    print(f"\nEpahh perdeste, que pena.\n\nO teu saldo ficou em {saldo}$.")
            if numero_sorteado % 2 != 0:
                if vermelho_ou_preto == 1:
                    print(f"\nEpahh perdeste, que pena.\n\nO teu saldo ficou em {saldo}$.")
                elif vermelho_ou_preto == 2:
                    valor_ganho = valor_apostado + valor_apostado * 0.5
                    saldo += valor_ganho
                    print(f"\nBoa!! Calhou um número preto!! Ganhaste {valor_ganho}$, e ficaste com {saldo}$ de saldo.")
        if jogo_roleta == 3:
            numero_certo = int(input("\nPretendes apostar que vai calhar qual número??\n\nR: "))
            if numero_certo == numero_sorteado:
                valor_ganho = valor_apostado + valor_apostado * 3
                saldo += valor_ganho
                print(f"\nBoa!!! Calhou te o número exato!! Ganhaste {valor_ganho}$, e ficaste com {saldo}$!!")
            elif numero_certo != numero_sorteado:
                print(f"\nEpahh perdeste, que pena. Saiu o número {numero_sorteado}, e escolheste o número {numero_certo}. \n\nO teu saldo ficou em {saldo}$.")
        if saldo <= 0:
            time.sleep(2)
            print("\nJá não tens mais saldo, ACABOU-SE.")
        else:
            rov = int(input("\nRodar outra vez??\n\n - Sim (1)\n - Não (2)\n\nR: "))
            if rov == 1:
                roleta(saldo)
            elif rov == 2:
                print(f"\nObrigado por jogares nos slots!! Sempre saíste da roleta com {saldo}$!! Continuação!!")
            else:
                print("\nO programa terminou!! Saíste da roleta!!!")
        
        return saldo

    roleta(saldo)

except:
    print("\nERRO")