class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def getnome(self):
       return self.nome

    def getvalor(self):
       return self.valor

    def setnome(self, novonome):
       self.nome = novonome

    def setvalor(self, novovalor):
       self.valor = novovalor
