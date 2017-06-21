qtd=int(input("Quantas idades você deseja inserir? "))
for i in range(qtd):
    id=input("Insira sua idade: ")
    if i==0:
        mi=id
    if id>mi:
        mi=id
print("A maior idade é: ",mi)
