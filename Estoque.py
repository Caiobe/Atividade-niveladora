class Estoque:
    def __init__(self,quantidades,produtos):
        self.quantidades = quantidades
        self.produtos = produtos

    def checarProduto (self,nomeDoProduto,quantidade):
        produtopresente = False
        for item in self.produtos:
            if item.nome == nomeDoProduto:
                produtopresente = True
                break
        if produtopresente == True:
            if quantidade <= self.quantidades[nomeDoProduto]:
                return True
            else:
                print('erro: excedido limite do estoque')
                return False
        else:
            print('Produto não está presente no estoque')
            return
    def retirarProduto (self,nomeDoProduto,quantidade):
        if self.checarProduto(nomeDoProduto,quantidade) == True:
            self.quantidades[nomeDoProduto] -= quantidade
        else:
            print('Não há produto suficiente.')
    def listarProdutos (self):
        for item in self.produtos:
            print(f"{item.nome} valor:{item.valor} quantidade: {self.quantidades[item.nome]}")
