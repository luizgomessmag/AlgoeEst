nome=input("insira o seu nome ")
idade=int(input("insira a sua idade "))
turma=int(input("insira a sua turma "))

print(f"Aluno cadastrado com sucesso:{nome}, {idade} anos, turma {turma}.")

if idade>6:
    print("matrícula validada")
else:
    print("matrícula invalidada")