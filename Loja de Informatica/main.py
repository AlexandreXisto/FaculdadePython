#Inicio do cod
print('Bem vindo ao mercado Haytech Delivery!!')
print('')
nome = input('Digite o nome do cliente: ')
print('O que o senhor gostaria de comprar? ')
print('')
compra = int(input('Teclados(1), Microfones(2) ou Mouses(3)? '))
if (compra == 1):
   qtd = int(input('Quantas unidades o senhor gostaria de solicitar? '))
   compra = qtd * 20
   print('{}, o total a pagar é de: {}R$'.format(nome,compra))
if (compra == 2):
   qtd =  int(input('Quantas unidades o senhor gostaria de solicitar? '))
   compra = qtd * 15
   print('{}, o total a pagar é de: {}R$'.format(nome,compra))
if (compra == 3):
   qtd = int(input('Quantas unidades o senhor gostaria de solicitar? '))
   compra = qtd * 20
   print('{}, o total a pagar é de: {}R$'.format(nome,compra))
else:
   print('Pedido Inválido!')
#Fim do codigo