# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# quantas pessoas tem mais de 18 anos;
# quantos homens foram cadastrados;
# quantas mulheres tem menos de 20 anos.
cont = idcont = homemcont = mulhercont = 0
while True:
    cont +=1
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        idcont +=1
    sexo = '0'
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]')).upper().strip()[0]
    if sexo == 'M':
        homemcont +=1
    elif sexo == 'F':
        if idade < 20:
            mulhercont +=1
    continuar = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        print('-=-=-=-='*5)
    if continuar == 'N':
        break
print(f'Foram cadastradas {cont} pessoas, sendo:\n'
      f'{homemcont} homens;\n'
      f'{idcont} maiores de 18 anos;\n'
      f'{mulhercont} mulheres menores de 20 anos.')