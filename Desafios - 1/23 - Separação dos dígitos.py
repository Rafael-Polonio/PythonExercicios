# Faça um programa que leia um número de 0 até 9999
# e mostre na sua tela cada um dos digitos separados
# Ex: 2183.  Unidade: 3. Dezena:8. Centena: 1. Milhar: 2.

n = str(input('Insira um número de 0 até 9999: '))

u = n[3]
d = n[2]
c = n[1]
m = n[0]

print(f'Milhares: {m}\n'
      f'Centenas: {c}\n'
      f'Dezenas: {d}\n'
      f'Unidades: {u}')