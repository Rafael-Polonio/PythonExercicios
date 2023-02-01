# Faça um programa que leia o cateto oposto e o cateto adjacente de um triangulo retângulo,
# calcule e mostre o comprimento da hipotenusa

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

from math import hypot

hp = hypot(ca,co)
print(f'A hipotenusa é {hp}')