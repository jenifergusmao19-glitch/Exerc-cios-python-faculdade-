# ==========================================
# EXERCÍCIO 1
# Leia dois números e exiba a soma, subtração, multiplicação e divisão.
# ==========================================
print("--- Exercício 1 ---")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {divisao}")
else:
    print("Divisão: Não é possível dividir por zero.")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 2
# Leia o nome e a idade de uma pessoa e exiba uma mensagem.
# ==========================================
print("--- Exercício 2 ---")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos.")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 3
# Leia um número e informe se ele é positivo, negativo ou zero.
# ==========================================
print("--- Exercício 3 ---")
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 4
# Leia a nota de um aluno e informe se foi aprovado (nota >= 7) ou reprovado.
# ==========================================
print("--- Exercício 4 ---")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aluno APROVADO!")
else:
    print("Aluno REPROVADO.")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 5
# Leia um número inteiro e mostre sua tabuada de 1 a 10.
# ==========================================
print("--- Exercício 5 ---")
tabrada_num = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{tabrada_num} x {i} = {tabrada_num * i}")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 6
# Leia um número N e calcule a soma dos números de 1 até N.
# ==========================================
print("--- Exercício 6 ---")
n = int(input("Digite um número N positivo: "))
soma_n = 0

for i in range(1, n + 1):
    soma_n += i

print(f"A soma de 1 até {n} é: {soma_n}")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 7
# Leia 10 números e informe a soma e a média.
# ==========================================
print("--- Exercício 7 ---")
soma_10 = 0

for i in range(1, 11):
    val = float(input(f"Digite o {i}º número: "))
    soma_10 += val

media_10 = soma_10 / 10
print(f"Soma total: {soma_10}")
print(f"Média: {media_10}")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 8
# Leia vários números até que o usuário digite 0. Informe a soma dos valores.
# ==========================================
print("--- Exercício 8 ---")
soma_loop = 0

while True:
    val = float(input("Digite um número (ou 0 para parar): "))
    if val == 0:
        break
    soma_loop += val

print(f"A soma dos números digitados é: {soma_loop}")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 9
# Crie uma função que receba dois números e retorne o maior deles.
# ==========================================
print("--- Exercício 9 ---")

def retornar_maior(a, b):
    if a > b:
        return a
    else:
        return b

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
maior = retornar_maior(n1, n2)

print(f"O maior número é: {maior}")

print("\n" + "="*40 + "\n")


# ==========================================
# EXERCÍCIO 10 (DESAFIO)
# Faça um programa que leia 5 números e informe o maior e o menor valor.
# ==========================================
print("--- Exercício 10 (Desafio) ---")

numeros = []
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

maior_valor = max(numeros)
menor_valor = min(numeros)

print(f"O maior valor digitado foi: {maior_valor}")
print(f"O menor valor digitado foi: {menor_valor}")
