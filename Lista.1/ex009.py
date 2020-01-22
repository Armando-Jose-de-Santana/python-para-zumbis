km_percorridos = float(input('Quilômetros percorridos: '))
aluguel = int(input('Dias de aluguel: '))
preco = km_percorridos * 0.15 + aluguel * 60
print(f'Preço a pagar: R${preco:.2f}')
