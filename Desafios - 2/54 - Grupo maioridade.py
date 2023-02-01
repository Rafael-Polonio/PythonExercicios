# Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de idade.
# Considere a maioriade com 21 anos.
tma = tme = 0
from datetime import date
hoje = date.today().year
for c in range (0,7):
    nasc = int(input('Digite o ano de seu nascimento: '))
    idade = hoje-nasc
    if idade>21:
        tma +=1
    else:
        tme +=1
print(f'Do total coletado, {tma} pessoas são maiores de idade e {tme} são menores de idade')