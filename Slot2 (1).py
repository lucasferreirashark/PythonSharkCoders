import time
from random import randint
saldo = 100

try:
    def slots(saldo):
        # Mostra o saldo do jogador
        print(f"\nTens {saldo}$ de saldo!!")
        # Define valor apostado pelo jogador
        valor_apostado = float(input("\nQual é o valor que queres apostar?\n\nR: "))
        # Enquanto o valor apostado for maior que o saldo ou o valor apostado for 0, pede ao jogador outro valor para apostar
        while valor_apostado > saldo or valor_apostado == 0:
            valor_apostado = float(input("\nAhh seu malandro, tu sabes o que fizeste, aposta outro valor!!\n\nR: "))
        # Caso o jogador queira apostar o saldo o saldo t0do, pedimos ao jogador para confirmar outra vez
        while valor_apostado == saldo:
            apostar_saldo = int(input("\nTens a certeza de que queres apostar o teu saldo todo??\n\n - Sim (1)\n - Não (2)\n\nR: "))
            if apostar_saldo == 2:
                valor_apostado = float(input("\nQual é o valor que queres apostar?\n\nR: "))
            else:
                break
        # Retira do saldo o valor apostado
        saldo -= valor_apostado
        # O programa define 3 números para os 3 spots
        lista_numeros = []
        for x in range(3):
            numeros = randint(1,10)
            lista_numeros.append(numeros)
        # Imprime-se espaço branco para ficar mais giro
        print(" ")
        # Imprime os três números na mesma linha, com um cooldown de 1 segundo entre cada número
        for x in lista_numeros:
            print([x], end="  ")
            time.sleep(1)
        # Caso os 3 números tenham sido iguais, damos ao jogador 3 vezes o valor apostado e adicionamos ao saldo
        if lista_numeros[0] == lista_numeros[1] and lista_numeros[1] == lista_numeros[2]:
            valor_ganho = valor_apostado * 3
            saldo += valor_ganho
            print(f"\n3 IGUAIS!! O valor ganho é de {valor_ganho}$.\n\nO teu saldo ficou em {saldo}$.")
        # Caso os 3 números tenham sido 7, damos ao jogador 200 vezes o valor apostado e adicionamos ao saldo
        elif lista_numeros[0] == 7 and lista_numeros[1] == 7 and lista_numeros[2] == 7:
            valor_ganho = valor_apostado * 200
            saldo += valor_ganho
            print(f"\nSETEE!! O valor ganho é de um GRANDE {valor_ganho}$.\n\nO teu saldo ficou em {saldo}$.")
        # Caso calhem 2 números iguais, damos ao jogador metade do valor apostado e adicionamos ao saldo
        elif lista_numeros[0] == lista_numeros[1] or lista_numeros[1] == lista_numeros[2] or lista_numeros[0] == lista_numeros[2]:
            valor_ganho = valor_apostado * 0.5
            saldo += valor_ganho
            print(f"\n\nCalharam-te 2 números iguais!! O valor ganho é de {valor_ganho}$.\n\nO teu saldo ficou em {saldo}$.")
        # Caso ele o jogador tenha perdido, avisamos o jogador
        else:
            print(f"\n\nEpahh perdeste, que pena.\n\nO teu saldo ficou em {saldo}$.")
        # Caso o jogador tenha o saldo menor ou igual a 0, daos um cooldown de 2 segundos para suspense, e terminamos o código
        if saldo <= 0:
            time.sleep(2)
            print("\nJá não tens mais saldo, ACABOU-SE.")
        # Caso o jogador continue com dinheiro, rodamos o resto do código
        else:
            # Perguntamos ao jogador se quer rodar a slot outra vez
            rov = int(input("\nRodar outra vez??\n\n - Sim (1)\n - Não (2)\n\nR: "))
            # Caso ele queira rodar outra vez, rodamos a função outra vez
            if rov == 1:
                slots(saldo)
            # Caso ele não queira rodar outra vez, agradeçemos ao jogador por jogar e saímos da função
            elif rov == 2:
                print(f"\nObrigado por jogares nos slots!! Sempre saíste das SLOTS com {saldo}$!! Continuação!!")
            # Caso ambas as opções não forem escolhidas, o jogador escolheu a opção errada e saiu das SLOTS
            else:
                print("O programa terminou!! Saíste das slots!!")
        return saldo

    slots(saldo)

except:
    print("\nERRO")