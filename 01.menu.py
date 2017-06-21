def soma(n1,n2,n3):
   s=n1+n2+n3
   print("O resultado da soma dos números anteriormente é : ",a)

def maior(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("O maior número é o: ",a)
    elif n2>n1 and n2>n3:
        print("O maior número é o: ",b)
    else:
        print("O maior número é o: ",c)

def menor(n1,n2,n3):
    if n1<n2 and n1<n3:
        print("O menor número é o: ",a)
    elif n2<n1 and n2<n3:
        print("O menor número é o: ",b)
    else:
        print("O menor número é o: ",c)

def media(n1,n2,n3):
    med=(n1+n2+n3)/3
    print("A média dos números inseridos anteriormente é: %.2f"%(med))

def opcao(o):
  if o==1:
    soma(a,b,c)
  elif o==2:
    maior(a,b,c)
  elif o==3:
    menor(a,b,c)
  elif o==4:
    media(a,b,c)


a=int(input("Insira o primeira número:"))
b=int(input("Insira o segundo número:"))
c=int(input("Insira o terceiro número:"))

op=int(input("Escolha uma opção. Instruções: 1 - soma dos número, 2 - exibe o maior dos número, 3 - exibe o menor dos números, 4 - média dos números: "))

while op<=0 or op>4:
    op=int(input("Opção inválida. Escolha uma opção. Instruções: 1 - soma dos número, 2 - exibe o maior dos número, 3 - exibe o menor dos números, 4 - média dos números: "))
opcao(op)
