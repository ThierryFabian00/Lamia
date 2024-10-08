#Orientação a objetos
class Produto:
    def __init__(self, nome, preco = 1.99, desc=0):
        self.nome = nome # Dois __ significa atributo privado
        self.__preco = preco
        self.desc = desc
    
    @property #getter
    def preco(self):
        return f'R$ {self.__preco}'
    
    @preco.setter #setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
    
    @property # faz com que seja interpretado como uma variavel e nao um metodo
    def preco_final(self):
        return (1 - self.desc) * self.__preco
    
p1 = Produto('Caneta', 10, 0.1) #produto.__init__ (p1...)
p2 = Produto('Caderno', 14, 0.5)

p1.preco = 70.89
p2.preco = 17.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)
