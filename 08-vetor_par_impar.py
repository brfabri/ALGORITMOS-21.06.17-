vet=[]
par=[]
imp=[]

for i in range(20):
    vet.append(int(input("Insira um número: ")))
for i in range(20):
    if vet[i]%2==0:
        par.append(vet[i])
    else:
        imp.append(vet[i])
print(par)
print(imp)