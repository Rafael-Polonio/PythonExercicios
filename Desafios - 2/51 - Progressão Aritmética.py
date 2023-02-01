# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
último = primeiro + (10 - 1) * razao
for c in range(primeiro, último+razao, razao):
    print(f'{c}', end=' --> ')
print('Acabou!')