print('---------- Programa de divisão ------------')
print()

numero = float(input('Digite um número para dividir: '))
divisor = float(input('Digite o número divisor: '))

try:
    resultado = numero / divisor
    print('O resultado da divisão é: ',resultado)
except:
    print('Opsss! Não será possível dividir por zero!')
