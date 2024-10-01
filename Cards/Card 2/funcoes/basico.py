#Uma funcao define um bloco
def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome}! \nVc nem parece ter {idade} anos!')

#E melhor ter uma funcao que retorne um valor
def soma_e_multi(a, b, x):
    return a + b * x

#So executa se for o arquivo principal 
if __name__ == '__main__':
    saudacao('Ana', idade = 30)
    print(soma_e_multi(3,2,2))