'''
Exercicio 1
Crie um programa que recebe como entrada dois números reais.
O programa deve imprimir as quatros operações matemáticas entre os dois números (soma, subtração, divisão e multiplicação)
'''

# Solicita ao usuário para inserir dois números reais
num1 = float(input("Digite o primeiro número real: "))
num2 = float(input("Digite o segundo número real: "))

# Realiza as operações matemáticas
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

# Imprime os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")
print(f"Multiplicação: {multiplicacao}")
