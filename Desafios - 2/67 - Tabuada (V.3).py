# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número digitado for negativo.
contador = 0
while True:
    n = int(input('Digite um número (se o número for negativo, o programa parará): '))
    if n < 0:
        break
    print(f'-=-=-=- Tabuada de {n} -=-=-=-')
    for c in range (0,10):
        contador += 1
        print (f'{n} * {contador} = {n*contador}')