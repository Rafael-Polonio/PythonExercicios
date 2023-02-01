import math
#OU
from math import sqrt, floor, ceil

n = float(input('Digite um valor:'))

raiz = math.sqrt(n)

print(f'A raiz de {n} exata é {raiz}\n' 
      f'A raiz de {n} arredondada para baixo é {math.floor(raiz):.2f}\n'
      f'A raiz de {n} arredondada para cima é {math.ceil(raiz):.2f}')

#import random
#n2 = random.randint
#raizz = math.sqrt(n2)
#print(f'a raiz de {n2} é {raizz}')