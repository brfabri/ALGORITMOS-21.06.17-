diasv=int(input("Insira quantos dias de vida você tem: "))
anos=diasv/365
mes=(diasv%365)/30
dias=((diasv%365)%30)

print("Você tem %1.f anos %1.f meses e %1.f dias de vida."%(anos,mes,dias))

