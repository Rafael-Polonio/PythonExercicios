# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: sênior
# Acima de 20 anos: master

from datetime import date
hoje = date.today().year
n = int(input('Digite seu ano de nascimento: '))
idade = hoje-n
if idade <= 9:
    print('Mirin')
elif idade <= 14:
    print('Infantil')
elif idade <=19:
    print('Júnior')
elif idade <=20:
    print('Sênior')
else:
    print('Master')