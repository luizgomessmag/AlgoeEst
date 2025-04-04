idade=int(input("insira a sua idade "))
genero=(input("insira o seu gênero "))
atleta=(input("você é atleta? "))

if idade<15:
    print("artigos infantís")
else:
    if idade>15 and idade<=21 and genero=="feminino":
        print("Maquiagens e moda")
    else:
        if idade>15 and idade<=32 and genero=="masculino" and atleta=="sim":
            print("artigos esportivos")
        else:
            if idade>15 and idade<=21 and genero=="masculino" and atleta=="não":
                print("videogames")
            else:
                if idade>=21 and idade<=32 and genero=="masculino" and atleta=="não":
                    print("jardinagem e eletrodomesticos")
                else:
                    if idade>=22 and idade<=35 and genero=="feminino":
                        print("artigos esportivos e itens de casa")
                    
