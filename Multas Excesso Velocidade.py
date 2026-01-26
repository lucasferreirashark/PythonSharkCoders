limite = int(input("Qual é o limite de velocidade?\n\nR: "))
velocidade = int(input("\nQual era a velocidade a que o sujeito se encontrava?\n\nR: "))

if velocidade > limite:
    velocidade_extra = velocidade - limite
    valor_multa = velocidade_extra * 2
    print(f"\nO sujeito estava acima do limite de velocidade de {limite} km/h, por {velocidade_extra} km/h, então recebeu uma multa de {valor_multa}$")
else:
    print("\nO sujeito estava dentro do limite!! Nenhuma multa foi aplicada!!")