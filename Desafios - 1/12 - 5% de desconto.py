# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Digite o preço do produto: '))
d = p*0.05
pd = p-d
print(f'Se o preço é {p}\n'
      f'o desconto será de {d}\n'
      f'portanto, o preço final será {pd}')