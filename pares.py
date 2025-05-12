print('---------- Programa que conta pares----------')
print()

contapares = 0
for contador in range(5):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        contapares += 1

print('Quantidade de pares:', contapares)
