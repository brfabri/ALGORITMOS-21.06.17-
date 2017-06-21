from random import randint
r=randint(0,10)
i=0
tent=11
while tent!=r:
    i=i+1
    tent=int(input("Insira o numero de 0 a 10: "))
print("Você acertou!!! Número de tentativas:",i)
