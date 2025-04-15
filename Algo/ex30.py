palavras=[]
palindromos=[]

for palavra in range(0,5):
    palavras.append(input("insira uma palavra "))

for palavra in palavras:
    palavracontrario=palavra[::-1]
    if palavracontrario==palavra:
        palindromos.append(palavra)

print(f'as palavras que são palíndromos são:{palindromos}')


    




