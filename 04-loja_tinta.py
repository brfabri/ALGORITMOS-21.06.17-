area=float(input("Insira o tamanho em metros quadrados da área a ser pintada: "))

if area%54==0:
    latas=area/54
else:
    latas=(area/54)+1
total=latas*80
print("Quantidade de latas: %2.d. Total: R$%2.f"%(latas,total))
