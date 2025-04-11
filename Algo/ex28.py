numeros=[]

for numero in range(0,8):
    numeros.append(int(input("insira um numero")))

for numero in numeros:
    if numero%2!=0:
        print(f"ímpar:{numero}")

for numero in numeros:
    if numero%2==0:
        print(f"par:{numero}")
