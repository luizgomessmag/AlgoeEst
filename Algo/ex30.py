#30. Encontrando Palíndromos
#- Crie uma lista chamada palavras com 5 palavras fornecidas pelo usuário.
#- Use um laço for para verificar quais palavras são palíndromos (ou seja, que podem ser lidas da mesma forma de trás para frente, como "arara").
#- Exiba as palavras palíndromas no final.


palavras=[]
palindromos=[]

for palavra in range(0,5):
    palavras.append(input("insira uma palavra "))

for palavra in palavras:
    palavracontrario=palavra[::-1]
    if palavracontrario==palavra:
        palindromos.append(palavra)

print(f'as palavras que são palíndromos são:{palindromos}')


    




