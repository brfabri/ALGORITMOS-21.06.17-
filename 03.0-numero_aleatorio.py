i=0
r=0
n=int(input("Insira um numero de 0 a 10: "))
tent=int(input("Insira o numero de tentativas: "))

while n!=r:
    i=i+1
    r=int(input("Insira o numero de 0 a 10: "))
if i>tent:
    print("Você acertou!!!. Seu número de tentativas foi maior ao definido inicialmente ")
elif i<tent:
    print("Você acertou!!!. Seu número de tentativas foi menor ao definido inicialmente ")
else:
    print("Você acertou!!!. Seu número de tentativas foi igual ao definido inicialmente ")


