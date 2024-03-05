'''
Exercicio 2
Crie um programa que recebe 2 números reais como entrada e um operador matemático. De acordo com o operador matemático fornecido, o programa deve calcular e apresentar o resultado da operação.

Exemplo

1 2 +

o resultado terá que sair

3
'''

# Solicita ao usuário para inserir dois números reais
num1 = float(input("Digite o primeiro número real: "))
num2 = float(input("Digite o segundo número real: "))

# Solicita ao usuário para inserir um operador matemático
operador = input("Digite o operador matemático (+, -, *, /): ")

# Verifica o operador e realiza a operação correspondente
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    # Verifica se o segundo número é zero para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
else:
    print("Operador inválido.")
    resultado = None

# Imprime o resultado, se não for None
if resultado is not None:
    print("Resultado:", resultado)