x = 10
#Para isso e mais recomendado o FOR
# while x:
#     print(x)
#     x -= 1

# print('Fim!')
      
total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota

print(f'A media da turma e {total // qtde}')
