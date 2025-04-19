print('----- programaque calcula a média -----')
print()

aluno = str(input('Digite o nome do aluno: '))
notat = float(input('Digite a nota teórica: '))
notap = float(input('Digite a nota prática: '))
notatr = float(input('Digite a nota do trabalho: '))

media = (notat + notap + notatr) / 3
print()
print(f'A média do aluno(a) {aluno} é: ', media)

if media >= 8:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')