cont=float(input("Insira o valor da conta: "))
pag=float(input("Insira o valor do pagamento: "))

notas=[50,20,10,5,2,1]

troco=pag-cont

for i in range(len(notas)):
    n=int(troco/notas[i])
    troco=troco%notas[i]
    if n!=0:
        print("%d nota(s) de R$ %.2f"%(n,notas[i]))

