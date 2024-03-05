"""
Imprimindo um unico caractere "*" por vez e ultilizando a estrutura de
repetição "for", crie um programa que imprima no console o texto abaixo:
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""
texto = ""

for i in range(2):
    texto += "*" * (i+1) + "\n"

print(texto)