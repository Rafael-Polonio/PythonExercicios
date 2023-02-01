# Faça um programa que leia um número inteiro e diga se ele é ou nao um número primo.

n = int(input('Digite um número: '))
tot = 0

for c in range(1, n+1):
    if n%c==0:
        print('\33[33m', end='')
        tot +=1
    else:
        print('\33[31m', end='')
    print(f'{c} ', end='')

if tot == 2:
    print(f'\n{n} é divisível {tot} vezes, por isso é um número primo!')
else:
    print(f'\n{n} é divisível {tot} vezes, por isso não é um número primo.')