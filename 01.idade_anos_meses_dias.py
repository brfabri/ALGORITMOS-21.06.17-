from datetime import datetime
now = datetime.now()

diaat=now.day
mesat=now.month
anoat=now.year

diaan=int(input("Insira o dia de seu nascimento: "))
mesan=int(input("Insira o mes de seu nascimento: "))
anoan=int(input("Insira o ano de seu nascimento: "))

idade=anoat-anoan

if  mesat>mesan:
    mes=mesat-mesan
    if diaan>diaat:
        qtddia=(30-diaan)+diaat
        qtdmes=mes-1
        print("Você têm ",idade," anos, ",qtdmes," meses e",qtddia," dias de vida")
    else:
        qtddia=diaat-diaan
        print("Você têm ",idade," anos, ",mes," meses e",qtddia," dias de vida")
elif  mesan>mesat:
    qtdanos=idade-1
    qtdmes=(12-mesan)+mesat
    if diaan>diaat:
        qtddia=(30-diaan)+diaat
        mes=qtdmes-1
        print("Você têm ",qtdanos," anos, ",qtdmes," meses e",qtddia," dias de vida")
    else:
        qtddia=diaat-diaan
        print("Você têm ",qtdanos," anos, ",qtdmes," meses e",qtddia," dias de vida")