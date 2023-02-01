# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média igual ou maior que  7.0: Aprovado.

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1+n2)/2

if m<5.0:
    print('Reprovado!')
elif m>6.9:
    print('Aprovado!')
else:
    print('Recuperação!')