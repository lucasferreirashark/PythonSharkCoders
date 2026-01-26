salario_base = int(input("Qual é o valor do salário base?\n\nR: "))

if salario_base < 100:
    print("\nInsere um salário a partir de 100$")
elif salario_base >= 100 and salario_base < 500:
    salario_final = salario_base * 1.15
    print(f"\nO salário final será {salario_final}$, com ajuste de 15%")
elif salario_base >= 500 and salario_base <= 1000:
    salario_final = salario_base * 1.10
    print(f"\nO salário final será {salario_final}$, com ajuste de 10%")
else:
    salario_final = salario_base * 1.05
    print(f"\nO salário final será {salario_final}$, com ajuste de 5%")
