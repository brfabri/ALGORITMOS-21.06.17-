ano=int(input("Insira ano: "))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("É bissexto")