notas=[]
media=0
for nota in range(0,5):
    notas.append(float(input("Insira a nota")))

for nota in notas:
    media=notas[0]+notas[1]+notas[2]+notas[3]+notas[4]/5

print(f"o valor da média é:{media}")
