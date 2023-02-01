# Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# Ex: a porção inteira de 6.9340 é 6

import math
n = float(input('Digite um número qualquer: '))
ni = math.trunc(n)
print(f'A porção inteira de {n} é {ni}')