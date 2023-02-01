# Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1,6):
    p = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p>maior:
            maior = p
        if p<menor:
            menor = p
print(f'O menor peso lido foi {menor} Kg, e o maior peso lido foi {maior} Kg')