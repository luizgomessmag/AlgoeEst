palavras=[]


for palavra in range(0,5):
    palavras.append(input("insira uma palavra"))

quant=0

for palavra in palavras:
    if len(palavra)> 5:
        quant=quant+1
print(f"a quantidade de palavras com mais de 5 caracteres é:{quant}")
