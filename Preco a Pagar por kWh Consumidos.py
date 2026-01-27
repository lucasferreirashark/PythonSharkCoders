residencia = input("Qual é o tipo da residência??\n\n - Residencial (R)\n - Comercial (C)\n - Industrial (I)\n\nR: ")
kwh_consumidos = int(input("\nQuantos kWh foram consumidos?\n\nR: "))

if residencia == "R":
    if kwh_consumidos <= 500 and kwh_consumidos > 0:
        preco_kwh = 0.4
    elif kwh_consumidos > 500:
        preco_kwh = 0.65
    else:
        print("A quantidade de kWh tem de ser acima de 0!!")

if residencia == "C":
    if kwh_consumidos <= 1000 and kwh_consumidos > 0:
        preco_kwh = 0.55
    elif kwh_consumidos > 1000:
        preco_kwh = 0.6
    else:
        print("A quantidade de kWh tem de ser acima de 0!!")

if residencia == "I":
    if kwh_consumidos <= 5000 and kwh_consumidos > 0:
        preco_kwh = 0.55
    elif kwh_consumidos > 5000:
        preco_kwh = 0.6
    else:
        print("A quantidade de kWh tem de ser acima de 0!!")

if residencia == "R":
    residencia_extenso = "Residencial"
elif residencia == "C":
    residencia_extenso = "Comercial"
else:
    residencia_extenso = "Industrial"

preco_pagar = preco_kwh * kwh_consumidos
print(f"O preço a pagar por {kwh_consumidos} kWh, numa residência tipo {residencia_extenso}, é de {preco_pagar}$")
