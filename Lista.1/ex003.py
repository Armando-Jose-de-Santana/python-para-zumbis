dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))

total_em_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos, correspondem à {total_em_segundos} segundos.')
