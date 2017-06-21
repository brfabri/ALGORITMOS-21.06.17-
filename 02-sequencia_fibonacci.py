f=[1,1]
n = int(input("Insira um número: "))
for i in range(n-2):
    f.append(f[i]+f[i+1])
print(f[-1])

