# crie um programa que leia o nome completo de uma pessoa e mostre
# o nome com todas as letras maiúsculas;
# o nome com todas as letras minúsculas;
# quantas letras ao todo (sem considerar espaços);
# quantas letras tem o primeiro nome.

n = str(input('Digite seu nome: '))
nu = n.upper()
nl = n.lower()
ns = len(n.strip())
n1 = n.split()
n2 = len(n1[0])

print(f'Todas letras maiúsculas: {nu}\n'
      f'Todas letras minúsculas: {nl}\n'
      f'Quantia de letras (sem espaços): {ns}\n'
      f'Quantia de letras no 1ª nome: {n2}')