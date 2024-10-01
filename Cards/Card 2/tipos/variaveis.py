a = 3
b = 4.4

print(a + b)

texto = 'Sua idade é...'
idade = 23

#print(texto + str(idade))
print(f'{texto} {idade}')
# fstring uma maneira de formatar strings, ela permitem a interpolação de variáveis e expressões diretamente dentro de uma string

saudacao = 'bom dia '
print(3 * saudacao)

PI = 3.14
#Em python nao existem constantes, usar letras maiusculas para costantes
raio = float(input('Informe o raio da circunferencia:'))
area = PI * pow(raio, 2) #funcao de potencia

print(f'A área da circ é {area} m2.')

