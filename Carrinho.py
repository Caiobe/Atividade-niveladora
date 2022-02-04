from Estoque import *

class Carrinho:
    def __init__(self):
        self.quantidades = {}
        self.produtos = []

    def checarProduto (self,nomeDoProduto,quantidade):
        produtopresente = False
        for item in self.produtos:
            if item == nomeDoProduto:
                produtopresente = True
                break
        if produtopresente == True:
            if quantidade <= self.quantidades[nomeDoProduto]:
                return True
            else:
                print('erro: excedido limite do carrinho')
                return False
        else:
            print('item não encontrado no carrinho')
            return

    def adicionarProduto (self,nomeDoProduto,quantidade,estoque):
        if estoque.checarProduto(nomeDoProduto,quantidade) == True:
            print('adicionado ' +  str(quantidade) + ' '+ nomeDoProduto +' ao carrinho')
            estoque.retirarProduto(nomeDoProduto,quantidade)

            if nomeDoProduto not in self.produtos:
                self.produtos.append(nomeDoProduto)
                self.quantidades[nomeDoProduto] = quantidade

            else:
                self.quantidades[nomeDoProduto] += quantidade

            print(self.quantidades[nomeDoProduto])
        else:
            return
    def retirarProduto (self, nomeDoProduto, quantidade):
        if self.checarProduto(nomeDoProduto,quantidade) == True:
            print('removido ' +  str(quantidade) + ' '+ nomeDoProduto +' do carrinho')
            self.quantidades[nomeDoProduto] -= quantidade

            print(self.quantidades[nomeDoProduto])

        else:

            return
