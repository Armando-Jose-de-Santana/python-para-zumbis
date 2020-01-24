n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n2 < n1 > n3:
    maior = n1
elif n1 < n2 > n3:
    maior = n2
else:
    maior = n3

if n2 > n1 < n3:
    menor = n1
elif n1 > n2 < n3:
    menor = n2
else:
    menor = n3

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
