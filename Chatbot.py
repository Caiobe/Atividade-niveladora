from Carrinho import *
from Estoque import *
class Chatbot:
    def __init__(self,carrinho,estoque):
        self.carrinho = carrinho
        self.estoque = estoque
    def iniciaPrograma(self):
        entrada = True
        nome = input('Insira o nome ')

        print(125 * '-')

        print(f'Ola, {nome}')

        print(125 * '-')

        print('Bem vindo ao chatbot de atendimento. Os seguintes comandos estão disponíveis')


        while entrada == True:

            print('1- Adicionar item')
            print('2- Remover item')
            print('3- Mostrar o carrinho')
            print("4- Fechar carrinho de compras")


            comando = int(input('insira seu comando '))
            if comando == 1:
                self.estoque.listarProdutos()
                produto = input('insira o nome do produto ')
                quantidade = int(input ('insira a quantidade '))
                if quantidade >= 0:
                    self.carrinho.adicionarProduto(produto,quantidade,self.estoque)
                else:
                    print('valor de quantidade inválido')
                    continue
            elif comando == 2:
                produto = input('insira o nome do produto ')
                quantidade = int(input('insira a quantidade '))

                self.carrinho.retirarProduto(produto, quantidade)

            elif comando == 4:
                entrada = False



