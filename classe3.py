class Smartphone:
    def __init__(self,marca, modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def ligar(acao):
        print('Fazendo chamada...')
        
print('---------- Programade de Classe aula 2 ----------')
print()

class Smartwatch(Smartphone):
    pass
    
relogio1 = Smartwatch('Xiaomi', 'Mi Mand 7', 'Preto')

print('Marca: ',relogio1.marca)
print('Modelo: ',relogio1.modelo)
print('Cor: ',relogio1.cor)