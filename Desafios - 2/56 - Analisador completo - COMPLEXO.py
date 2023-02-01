# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
# No final, mostre:
# a média de idade do grupo;
# Qual o nome do homem mais velho;
# quantas mulheres tem menos de 21 anos.
tsm = 0
tsf = 0
ti = 0
tsfmenor21 = 0
idadevelho = 0
nomevelho = ''
for c in range(0,4):
    print(f'------- {c}ª Pessoa --------')
    n = str(input('Nome: ')) #receber nome
    i = int(input('Idade: ')) #receber idade
    ti+=i
    s = str(input('Sexo [M/F]: ')).strip().upper() #receber sexo
    if s == 'M':
        tsm +=1 #calculo total de homens
        if c ==1: #se for o primeiro Homem da lista, os itens <idadevelho> e <nomevelho> serão preenchidos com seu conteúdo
            idadevelho = i
            nomevelho = n
        if i>idadevelho: #Se aparecer um Homem com idade maior que a do primeiro (do segundo, do terceiro...), <nomevelho> e <idadevelho> receberão um novo conteúdo
            idadevelho = i
            nomevelho = n
    elif s == 'F':
        tsf +=1 #calculo total de mulheres
        if i<21:
            tsfmenor21 +=1 #calculo total de mulheres menores de 21 anos
mi = ti/4 #média de idade do grupo
print(f'A média de idade é {mi}.\n'
      f'{nomevelho} é o homem mais velho, tendo {idadevelho} anos de idade\n'
      f'O total de pessoas do sexo masculino é {tsm},\n'
      f'e do feminino é {tsf}, sendo que destas últimas {tsfmenor21} são menores que 21 anos.')