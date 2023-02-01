# Faça um programa que calcule a soma de todos os números impares que são multiplos de três
# e que se encontram no intervalo de 1 até 500.
soma = 0
for c in range(0, 501):
    if c%2==1:
        if c%3==0:
            soma += c
            print(c)
print('-=-=-='*5)
print(f'A somatória de todos os números digitados é {soma}')