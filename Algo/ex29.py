valores=[]

for valor in range(0,4):
    valores.append(int(input("insira um valor")))

novovalor=int(input("insira um valor adicional"))

for valor in valores:
    valores=valor*novovalor
    print(valores)