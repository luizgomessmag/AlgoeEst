numeros=[]

for numero in range(0,10):
    numeros.append(int(input("Insira um numero")))

for numero in numeros:
    soma=numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]+numeros[5]+numeros[6]+numeros[7]+numeros[8]+numeros[9]
    print(f"a soma é:{soma}")