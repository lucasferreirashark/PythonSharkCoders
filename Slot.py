import time
from random import randint
saldo = 100

try:
    def slots():
        global saldo
        print(f"\nTens {saldo}$ de saldo!!")
        valor_apostado = int(input("\nQual é o valor que queres apostar?\n\nR: "))
        while valor_apostado > saldo or valor_apostado == 0:
            valor_apostado = int(input("\nAhh seu malandro, tu sabes o que fizeste, aposta outro valor!!\n\nR: "))
        saldo -= valor_apostado
        lista_numeros = []
        for x in range(3):
            numeros = randint(1,6)
            lista_numeros.append(numeros)
        print("")
        for x in lista_numeros:
            print([x], end="  ")
            time.sleep(1)
        if lista_numeros[0] == lista_numeros[1] and lista_numeros[1] == lista_numeros[2]:
            valor_ganho = valor_apostado * 3
            saldo += valor_ganho
            print(f"\nO valor ganho é de {valor_ganho}$\n\nO teu saldo ficou em {saldo}$.")
        elif lista_numeros[0] == 7 and lista_numeros[1] == 7 and lista_numeros[2] == 7:
            valor_ganho = valor_apostado * 200
            saldo += valor_ganho
            print(f"\nSETEE!! O valor ganho é de um GRANDE {valor_ganho}$\n\nO teu saldo ficou em {saldo}$.")
        elif lista_numeros[0] == lista_numeros[1] or lista_numeros[1] == lista_numeros[2]:
            valor_ganho = valor_apostado * 0.5
            saldo += valor_ganho
            print(f"\n\nCalharam-te 2 números iguais!! O valor ganho é de {valor_ganho}$\n\nO teu saldo ficou em {saldo}$.")
        else:
            print(f"\n\nEpahh perdeste, que pena.\n\nO teu saldo ficou em {saldo}$.")
        if saldo <= 0:
            time.sleep(3)
            print("\nJá não tens mais saldo, ACABOU-SE.")
        else:
            rov = input("\nRodar outra vez??\n\nR: ")
            while rov != "sim" or rov != "Sim" or rov != "s" or rov != "S":
                rov = input("\nVou perguntar outra vez, para ver se entendeste bem. Queres rodar outra vez??\n\nR: ")
                if rov == "sim" or rov == "Sim" or rov == "s" or rov == "S":
                    slots()

    slots()

except:
    print("\nERRO")