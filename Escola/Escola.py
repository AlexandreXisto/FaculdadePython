nome = (input('Digite o nome da criança: ')) #Entrando com os valores da criança
idade = int(input('Digite a idade da criança: '))


while ('s' != 0): #Usei laço de repetição para se o usuário desejar continuar
 if  (idade < 0) and (idade > 6):
    print('O aluno {} tem {} anos e esta no Ensino Infantil'.format(nome,idade))
 if (idade <= 6) and (idade > 11):
    print('O aluno {} tem {} anos e esta no Ensino Fundamental l'.format(nome,idade))
 if (idade <= 11) and (idade > 15):
    print('O aluno {} tem {} anos e esta no Ensino Fundamental ll'.format(nome,idade))
 if (idade <= 15):
    print('O aluno {} tem {} anos e esta no Ensino medio'.format(nome,idade))

    s = (input('Deseja continuar? 0 - Não 1 - Sim '))
    break #Para evitar o loop infinito



