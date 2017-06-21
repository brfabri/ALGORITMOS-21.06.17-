n=int(input("Insira um número de 1 até 10: "))
while n>10:
    n=int(input("Erro. Insira um número de 1 até 10: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)