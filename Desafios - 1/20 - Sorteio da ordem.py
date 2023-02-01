# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

a1 = str(input('Nome do aluno: '))
a2 = str(input('Nome do aluno: '))
a3 = str(input('Nome do aluno: '))
a4 = str(input('Nome do aluno: '))
lista = [a1,a2,a3,a4]
from random import shuffle
ordem = shuffle(lista)
print(f'A ordem de alunos sorteada é {lista}')
