print('Bem vindo a heavy Hayparty')
print('')
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
if nome == 'Vinicius':
    print('Vinicius! tudo bem? você ja é da casa!')
elif idade < 1 > 5:
    print('Você é menor de idade, não liberado!')
elif idade > 18:
    print('Seja bem vindo {} a Hayparty! divirta-se!'.format(nome))
elif idade > 100:
    print('Você esta mentindo sua idade!')