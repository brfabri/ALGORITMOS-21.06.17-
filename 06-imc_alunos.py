talt=0
tpes=0

qtd=int(input("Informe a quantidade de alunos: "))
for i in range(qtd):
    pes=float(input("Informe o peso do aluno: "))
    alt=float(input("Informe a altura do aluno: "))
    imc=round(pes/(alt*alt),1)
    print("IMC: ",imc)

    if i==0:
        ma=imc
        me=imc
    if imc>ma:
        ma=imc
    elif imc<me:
        me=imc

    tpes=tpes+pes
    talt=talt+alt

mdpes=tpes/qtd
mdalt=talt/qtd
print("A média dos pesos é:",mdpes)
print("A média das alturas é:",mdalt)
print("O maior imc é ",ma," e o menor é ",me)