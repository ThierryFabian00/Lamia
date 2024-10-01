for i in range(10):
    print(i, end=' ')

print('')

for i in range (1, 11):
    print(i, end=' ')
        #   inicio, fim, passo
print('')

for i in range (1, 11, 7):
    print(i, end=' ')

print('')

for i in range (20, 0, -3):
    print(i, end=' ')

print('')

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=' ')
# end por padrao e ENTRE mas pode ser alterado
print('')

texto = 'Python e muito massa!'

for letra in texto:
    print(letra, end=' ')

print('')

for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')

print('')
produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5

}
for atrib in produto:
    print(atrib, ' ==> ', produto[atrib], end=' ')

print('')

for atrib, valor in produto.items():
    print(atrib, ' ==> ', valor, end=' ')

print('')

for valor in produto.values():
    [print(valor, end=' ')]

print('')

for atrib in produto.keys():
    [print(valor, end=' ')]