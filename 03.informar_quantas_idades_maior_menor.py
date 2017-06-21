qtd=int(input("Quantas idades você deseja inserir? "))
for i in range(qtd):
    id=input("Insira sua idade: ")
    if i==0:
        mi=id
        mni=id
    if id>mi:
        mi=id
    elif id<mni:
        mni=id

print("A maior idade é: ",mi)
print("A menor idade é: ",mni)

