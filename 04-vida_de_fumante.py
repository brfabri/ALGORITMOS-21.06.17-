qtdc = int(input("Insira a quantidade de cigarros que você fuma por dia: "))
qtda = int(input("Insira a quantos anos você fuma: "))

tdia=qtdc*(qtda*365)
tmin=tdia*10
tempo=(tmin/60)/24
print("Você perdeu %.2f dias vida"%(tempo))