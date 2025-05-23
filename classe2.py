class Smartphone:
    def __init__(self,marca, modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def ligar(acao):
        print('Fazendo chamada...')
        
print('---------- Programade de Classe aula 2 ----------')
print()

marca = input('Digite a marca: ')
modelo = input('Digite o modelo: ')
cor = input('Digite a cor: ')
print('--------------------')

celular1 = Smartphone(marca, modelo, cor)
print('Marca: ',celular1.marca)
print('Modelo: ',celular1.modelo)
print('Cor: ',celular1.cor)
print('--------------------')
celular1.ligar()