# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
# ou então o empréstimo será negado

vc = float(input('Valor da casa: '))
sa = float(input('Seu salário: '))
du = int(input('Em quantos anos o valor do empréstimo será quitado: '))

prest = vc/(du*12)


if prest > (sa*0.3):
    print('Seu empréstimo foi negado')
else:
    print('Seu empréstimo foi aporvado')