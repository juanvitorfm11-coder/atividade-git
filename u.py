hora = float(input("Valor da hora: "))
horas = float(input("Horas trabalhadas: "))

salario = hora * horas

# IR
if salario <= 900:
    ir = 0

elif salario <= 1500:
    ir = salario * 0.05

elif salario <= 2500:
    ir = salario * 0.10

else:
    ir = salario * 0.20

sindicato = salario * 0.03
fgts = salario * 0.11

descontos = ir + sindicato
liquido = salario - descontos

print("Salário Bruto:", salario)
print("IR:", ir)
print("Sindicato:", sindicato)
print("FGTS:", fgts)
print("Salário Líquido:", liquido)
