nome=input("insira o nome do produto ")
quantidade=int(input("insira a quantidade comprada "))
preco=float(input("insira o preço do produto "))

total=quantidade*preco

if total>100:
    total=total*0.05


print(f"o valor total é:{total}")

    