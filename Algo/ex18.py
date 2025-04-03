salariob=float(input("insira o seu salario base"))
horaex=int(input("insira as horas extras trabalhadas"))
valorph=float(input("insira o valor pago por hora extra"))

valorex=horaex*valorph

salariototal=salariob+valorex

print(f"O seu salário com horas extras é de{salariototal}")
