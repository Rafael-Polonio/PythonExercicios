#Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'a';
# em que posição ela aparece a primeira vez;
# em que posição ela aparece a última vez

f = str(input('Digite uma frase: '))

fc = f.count('a')
fl = f.find('a')+1   #+1 porque a contagem começa no n° 0.
fr = f.rfind('a')+1

print(f'A letra A parece {fc} vezes, sendo que\n'
      f'a sua primeira aparição é na posição {fl}\n'
      f'e sua última aparição é na posição {fr}')