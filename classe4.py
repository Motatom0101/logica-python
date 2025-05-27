class Smartphone:
    def __init__(self,marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def ligar(acao):
        print('Fazendo chamada...')
        
    def despertar(self):
        print('Despertador do celular tocando')
        
print('---------- Programade de Classe aula 3 ----------')
print()

class Smartwatch(Smartphone):
    def __init__(self,marca, modelo, cor, bussola):
        super().__init__(marca, modelo, cor)
        self.bussola = bussola
    def status(self):
        print('Mostrando Status de atividades...')
        
    def despertar(self):
        print('Despertador do relógio tocando')
    
relogio1 = Smartwatch('Xiaomi', 'Mi Mand 7', 'Preto', 'True')

print('Marca: ',relogio1.marca)
print('Modelo: ',relogio1.modelo)
print('Cor: ',relogio1.cor)
print('Sensor de bússola: ',relogio1.bussola)
print()
relogio1.status()
relogio1.despertar()