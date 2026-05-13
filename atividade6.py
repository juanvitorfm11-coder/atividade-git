#parte0
numero_1 = input("primeiro numero")
numero_2 = input("segundo numero")

if numero_1 > numero_2:
    print(f"{numero_1} e maior")
else:
    print(f"{numero_2} e maior ")
    


#Parte1

numero = float(input("Digite um valor: "))

if numero > 0:
    print("O valor é positivo")
else:
    print("O valor é negativo")

#parte2

letra = input("digite F ou M:")

if letra == "F":
    print("Feminino")

elif letra == "M":
    print("Masculino")

else:
    print("Sexo inválido")

#Parte3
Letra = input("Digite uma letra").lower()
if Letra in ("aeiou"):
    print("e uma vogal")
else:
    print ("e uma consoante")
#parte4
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Media:", media)

if media == 10:
    print("Aprovado com Distinção")

elif media >= 7:
    print("Aprovado")

else:
    print("Reprovado")

#parte5
num1 = float(input("primeiro numero"))
num2 = float(input("segundo numero"))
num3 = float(input("terceiro numero"))

if num1 > num2 and num1 > num3:
    maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3
  #menor

if num1 < num2 and num1 < num3:
    menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3
print(f"o maior numero e: {maior}")
print(f"o menor numero e: {menor}") 

#parte6
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

maior = num1
menor = num1

# Verificando o maior
if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

# Verificando o menor
if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print("Maior numero:", maior)
print("Menor numero:", menor)

#parte8
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

menor = produto1

if produto2 < menor:
    menor = produto2

if produto3 < menor:
    menor = produto3

print("O produto mais barato custa:", menor)

#parte9
turno = input("Digite seu turno (M/V/N): ")

if turno == "M":
    print("Bom Dia!")

elif turno == "V":
    print("Boa Tarde!")

elif turno == "N":
    print("Boa Noite!")

else:
    print("Valor Inválido!")

#parte10
salario = float(input("Digite o salário: "))

# Verificando percentual
if salario <= 240:
    percentual = 20

elif salario <= 750:
    percentual = 15

elif salario <= 1700:
    percentual = 10

else:
    percentual = 5

# Cálculos
aumento = salario * percentual / 100
novo_salario = salario + aumento

# Resultado
print("Salário antes do reajuste: R$", salario)
print("Percentual aplicado:", percentual, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)
#parte12
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
#Parte13
dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("Segund")

elif dia == 2:
    print("Terça")

elif dia == 3:
    print("Quarta")

elif dia == 4:
    print("Quinta")

elif dia == 5:
    print("Sexta")

elif dia == 6:
    print("Sabado")

elif dia == 7:
    print("Domingo")

else:
    print("Valor inválido")

#parte14
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

# Conceitos
if media >= 9:
    conceito = "A"
    resultado = "APROVADO"

elif media >= 7.5:
    conceito = "B"
    resultado = "APROVADO"

elif media >= 6:
    conceito = "C"
    resultado = "APROVADO"

elif media >= 4:
    conceito = "D"
    resultado = "REPROVADO"

else:
    conceito = "E"
    resultado = "REPROVADO"

print("Notas:", nota1, "e", nota2)
print("Média:", media)
print("Conceito:", conceito)
print("Resultado:", resultado)
#parte16
import math

print(" EQUAÇÃO DO 2 GRAU ")

# Entrada do valor de A
a = float(input("Digite o valor de A: "))

# Verifica se A e zero
if a == 0:
    print("A equaçao não é do segundo grau.")
else:
    # Entrada dos outros valores
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    # Calculo do delta
    delta = (b ** 2) - (4 * a * c)

    print(f"Delta = {delta}")

    # Verificaçoes do delta
    if delta < 0:
        print("A equaçao nao possui raízes reais.")

    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui apenas uma raiz real.")
        print(f"Raiz: {x}")

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print("A equaçao possui duas raizes reais.")
        print(f"Primeira raiz: {x1}")
        print(f"Segunda raiz: {x2}")
        #parte17
        print("Ano bissexto ")

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} e bissexto.")
else:
    print(f"O ano {ano} nao e bissexto.")