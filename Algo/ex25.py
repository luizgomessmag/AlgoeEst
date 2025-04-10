numeros=[]

for numero in range(0,6):
    numeros.append(int(input("Insira um numero")))
menor=numeros[0]
maior=numeros[5]
for numero in numeros:
    
    if numero<menor:
        menor=numero
    else:
        if numero>maior:
            maior=numero
print(f"o maior numero é:{maior}")

print(f"o menor numero é:{menor}")        