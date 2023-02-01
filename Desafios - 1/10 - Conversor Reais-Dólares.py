# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela consegue comprar;
# sendo que: US$ 1.00 == RS$5.07  (26/01/23)

d = float(input('Quanto dinheiro será convertido? '))
c = d/5.07
print(f'{d:.2f} reais se converterão em {c:.2f} dólares')