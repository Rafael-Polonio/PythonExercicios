# Faça um algoritimo que leia o salário de um funcionário
# e mostre seu novo salário com 5% de aumento

n = float(input('Digite seu salário: '))
a = (n*0.05)
na = n + a
print(f'Se seu salário é {n},\n'
      f'5% de aumento corresponderá ao valor absoluto de {a}\n'
      f'portanto, seu salário com aumento será {na}')