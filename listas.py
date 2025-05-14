roupas = ['Camisa','Vestido','Saia','Bermuda','Calça']

roupa = input('Digite o nome da peça que busca: ')

if roupa in roupas:
    print('Encontrada: ',roupa)
else:
    print('Peça não encontrada. Continue buscando!')
    