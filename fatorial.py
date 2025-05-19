print('---------- Programa que calcula o fatorial ----------')
print()
 
def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1) 
    
print(fatorial(5))