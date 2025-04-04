idade=int(input("insira sua idade "))
acompanhado=(input("você está acompanhado de um membro ?"))
membro=(input("você é membro do clube ?"))

if idade<18:
    print("você não pode ter acesso ao clube.")
else:
    print("você é maior de idade.")
    if membro=="sim":
        print("você não paga pela entrada")
    else:
        print("você deve pagar pelo ingresso")
        if acompanhado=="sim" and membro=="sim":
            print("bem-vindo!")
        else:
            if acompanhado=="sim" and membro=="não":
                print("você paga metade do valor")
        