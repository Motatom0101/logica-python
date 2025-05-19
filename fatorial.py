print('---------- Programa que calcula o fatorial ----------')
print()
 
def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1) 

num = int(input('Digite um número: '))    
print(fatorial(num))
