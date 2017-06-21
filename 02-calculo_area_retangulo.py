base=int(input("Insira a base: "))
altura=int(input("Insira a altura: "))
area=base*altura
if base!=altura:
    print("A area do retangulo é: ",area)
else:
    print("A area do quadrado é: ",area)