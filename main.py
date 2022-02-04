from Produto import *
from Chatbot import *

produto1 = Produto('prego', 22.90)
produto2 = Produto('macaco', 11.25)
produto3 = Produto('esponja', 55.58)
produto4 = Produto('tarzan', 4.50)

produtos = [produto1, produto2, produto3, produto4]

quantidades = {"prego": 25, 'macaco': 2, 'esponja': 4, 'tarzan': 88}

produtosLista = []


estoque = Estoque(quantidades,produtos)

carrinho = Carrinho()

chatbot = Chatbot(carrinho,estoque)

chatbot.iniciaPrograma()






