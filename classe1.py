class Smartphone: #Classe
    marca = 'Apple' #Atributos
    modelo = 'Iphone 13'
    cor = 'Branco'
    
    def email(acao): #Método
        print('Enviando um email...')
    
print('---------- Programa de Classe aula 1 ----------')
print()

celular1 = Smartphone() #Instanciando o objeto
print('Marca: ',celular1.marca)
print('Modelo: ',celular1.modelo)
print('Cor: ',celular1.cor)
print()
celular1.email() #Chamando o método no objeto

print('---------- Celular 2 ----------')
print()

celular2 = Smartphone() #Instanciando o 2º objeto
celular2.marca = input('Digite a marca: ')
celular2.modelo = input('Digite o modelo: ')
celular2.cor = input('Digite a cor: ')
print()
print('Marca: ',celular2.marca)
print('Modelo: ',celular2.modelo)
print('Cor: ',celular2.cor)