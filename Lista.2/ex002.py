ano = int(input('Digite o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano digitado É BISSEXTO.')
else:
    print('O ano digitado NÃO É BISSEXTO.')
