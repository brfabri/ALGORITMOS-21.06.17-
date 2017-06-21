vet=[]
tev=[]
x = -1
for i in range(10):
    vet.append(float(input("Insira um número: ")))

tev=vet[:]

for i in range(10):
    tev[i]=vet[x]
    x=x-1
print(tev)




