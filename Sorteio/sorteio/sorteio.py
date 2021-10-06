nome = ['Alexandre']
lista = []
for i in range (3):
 valor = int(input('Digite o valor da contribuição: '))
 if valor >= 20:
    nome.append(input('Digite o seu nome: '))
    continue
    sorteado = random.choice(nome)
    print(sorteado)
 else:
    print('Voce não poderá participar do sorteio')



