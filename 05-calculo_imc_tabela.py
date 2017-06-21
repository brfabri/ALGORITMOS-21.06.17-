s=0
while s!="m" and s!="f":
    s = input("Insira seu sexo( 'm' para masculino e 'f' para feminino): ")
altura=float(input("Insira sua altura: "))
peso=float(input("Insira seu peso: "))
imc=peso/(altura*altura)
imc=round(imc,2)

print("IMC:",imc)

if s=="f":
    if imc<19.1:
        print("Abaixo do peso ideal")
    elif imc>=19.1 and imc<=25.8:
        print("Peso ideal")
    elif imc>25.8 and imc<=27.3:
        print("Pouco acima do peso ideal")
    elif imc>27.3 and imc<=32.3:
        print("Acima do peso ideal ")
elif s=="m":
    if imc<20.7:
        print("Abaixo do peso ideal")
    elif imc>=20.7 and imc<=26.4:
        print("Peso ideal")
    elif imc>25.4 and imc<=27.8:
        print("Pouco acima do peso ideal")
    elif imc>27.8 and imc<=31:
        print("Acima do peso ideal ")




