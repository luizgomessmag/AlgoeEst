sorteio=int(input("escolha um numero de 1 a 20 "))
palpites=[]
palpite=0

palpite=int(input("insira seu palpite "))
palpites.append(palpite)

while palpite!=sorteio:

    print("você errou")
    palpite=int(input("insira seu palpite "))
    palpites.append(palpite)
        

    

else:
    print(f"você acertou, o valor era: {sorteio}")
    print(f"seus palpites foram:{palpites}")

