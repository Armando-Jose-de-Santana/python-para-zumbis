preço = float(input('Informe o valor do produto: '))
percentagem = float(input('Informe a percentagem de desconto: '))

novo_preço = preço - (preço * percentagem / 100)

print(f'O produto que custava R${preço:.2f} com {percentagem}% de desconto, passa a custar R${novo_preço:.2f}')
