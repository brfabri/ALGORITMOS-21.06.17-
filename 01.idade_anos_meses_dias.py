from datetime import datetime
now = datetime.now()

diaat=now.day
mesat=now.month
anoat=now.year

diaan=int(input("Insira o dia de seu nascimento: "))
mesan=int(input("Insira o mes de seu nascimento: "))
anoan=int(input("Insira o ano de seu nascimento: "))

idade=anoat-anoan

if  mesan<mesat:
    qtdmes=mesat-mesan
    print("Você têm ",idade," anos, ",qtdmes," meses de vida")
elif  mesan>mesat:
    print(idade-1)
elif diaan==diaat or diaan<diaat and mesan==mesat:
    print(idade)
else:
    print(idade-1)
