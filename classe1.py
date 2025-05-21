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
