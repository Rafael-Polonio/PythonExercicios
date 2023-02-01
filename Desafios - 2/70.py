# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário quer continuar.
# No final, mostre:
# Qual é o total gasto na compra;
# quantos produtos custam mais R$1000,00
# qual é o nome do produto mais barato.
c = somapreço = mais1000 = 0
nomemenorpreço = ' '
while True:
    c += 1
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o preço do produto: '))
    somapreço += preço
    if c == 1:
        menorpreço = preço
        nomemenorpreço = nome
    else:
        if preço < menorpreço:
            menorpreço = preço
            nomemenorpreço = nome
    if preço > 1000.00:
        mais1000 += 1
    continuar = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram comprados {c} produtos, sendo que o\n preço total da compra {somapreço}.\n'
      f'{nomemenorpreço} foi o item comprado de menor preço, que custou {menorpreço};\n'
      f'E foram comprados {mais1000} itens de preço maior que R$1000,00.')