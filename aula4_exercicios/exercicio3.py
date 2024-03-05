'''
crie um programa que execute repetidamente o programa do exercicio 2. Após a apresentação do resultado
o programa deve perguntar se o usuário deseja continuar a calcular, se a resposta for S (sim) o programa deve continuar, se a resposta for N (não)
o programa deve terminar.
'''

while True:
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
            continue
    else:
        print("Operador inválido.")
        continue

    # Imprime o resultado
    print("Resultado:", resultado)

    # Pergunta ao usuário se deseja continuar calculando
    continuar = input("Deseja continuar calculando? (S/N): ").upper()
    while continuar not in ['S', 'N']:
        print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
        continuar = input("Deseja continuar calculando? (S/N): ").upper()

    # Se o usuário escolher 'N', o loop é interrompido
    if continuar == 'N':
        break
