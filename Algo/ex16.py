nota1=float(input("insira a sua nota"))
nota2=float(input("insira a sua nota"))
nota3=float(input("insira a sua nota"))

media=nota1+nota2+nota3/3

if media>=7:
    print("aprovado")

else:
    if media>=5 and media<7:
        print("em recuperação")

    else:
        print("reprovado")    
