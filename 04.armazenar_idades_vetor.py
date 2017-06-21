qtd=int(input("Quantas idades você deseja inserir? "))
idvet = list(range(qtd))
for i in range(qtd):
    id=input("Insira uma idade: ")
    idvet[i]=id
    if i==0:
        mi=idvet[i]
        mni=idvet[i]
    if idvet[i]>mi:
        mi=idvet[i]
    elif idvet[i]<mni:
        mni=idvet[i]

print("A maior idade é: ",mi)
print("A menor idade é: ",mni)
print("Todas as idades inseridas: ",idvet)
