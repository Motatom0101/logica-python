print('----------- Conversor de temperatura ----------')
print()

def converter(celsius):
    return (celsius * 9 / 5) + 32

valor = float(input('Digite o valor de graus Celsius: '))
print('O resultado da conversão é: ', converter(valor))
