nome = (input('Digite o nome do aluno: '))
nota = float(input('Digite a nota do aluno: '))
print('Digite "s" para sair')

while (nota != 's'):
 if (nota <= 2.9):
    print('O aluno {} tirou nota {} e se enquadra no conceito E'.format(nome,nota))
 if nota <= 4.9:
    print('O aluno {} tirou nota {} e se enquadra no conceito D'.format(nome,nota))
 if nota <= 6.9:
    print('O aluno {} tirou nota {} e se enquadra no conceito C'.format(nome,nota))
 if nota <= 8.9:
    print('O aluno {} tirou nota {} e se enquadra no conceito B'.format(nome,nota))
 if nota <= 10:
    print('O aluno {} tirou nota {} e se enquadra no conceito A'.format(nome,nota))
 break