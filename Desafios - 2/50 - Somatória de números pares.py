# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

s = 0
for c in range(0,7):
    n = int(input(('Digite um número inteiro: ')))
    if n%2==0:
        s += n
print(f'A somatória dos números pares é {s}')