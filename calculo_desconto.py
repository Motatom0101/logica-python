print('---------- Cálculo de desconto ----------')

menu = 'yes'
while menu == 'yes':
    valor = float(input('Digite um valor: '))
    percentual = float(input('Digite um percentual: '))/100
    resultado = valor * percentual
    
    print('O desconto é de: ', resultado)
    print()
    menu = input('Digite "yes" para continuar ou "no" para sair: ')
    