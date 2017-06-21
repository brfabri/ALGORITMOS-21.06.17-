a=int(input("Insira a medida do lado 'a' do triangulo: "))
b=int(input("Insira a medida do lado 'b' do triangulo: "))
c=int(input("Insira a medida do lado 'c' do triangulo: "))

if a!=b and a!=c and b!=c:
    print("Escaleno")
elif a==b or b==c or c==a:
    print("Isósceles")
elif a==b and a==c and b==c:
    print("Equilátero")
