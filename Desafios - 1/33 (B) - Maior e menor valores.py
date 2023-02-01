# Faça um programa que leia 3 números
# e qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um terceiro número: '))

if n1>n2:
    if n1<n2:
        if n1<n3:
            print(f'{n1} é o menor número!')
    if n1>n3:
        print(f'{n1} é o maior número!')
else:
    if n2>n1:
        if n2>n3:
            print (f'{n2} é o maior número!')
    if n3>n1:
        if n3>n2:
            print(f'{n3} é o maior número!')

if n1<n2:
    if n1<n3:
        print(f'{n1} é o menor número!')
if n2<n1:
    if n2<n3:
        print(f'{n2} é o menor número!')
if n3<n1:
    if n3<n2:
        print(f'{n3} é o menor número!')
