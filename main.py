# lista de frutas
frutas = ['Maracujá', 'Maçã', 'Laranja', 'Banana', 'Uva', 'Abacaxi']

# exibe a lista e o índice
for i in range(len(frutas)):
    print(f'Fruta de índice {i}: {frutas[i]}.')

# Usuário informa o índice do item a ser separado
indice = int(input('Informe o indice que deseja separar: ' ))

# separa o item
fruta = frutas.pop(indice)

#exibe o item separado
print(f'\n{fruta} foi separado!\n')

for i in range(len(frutas)):
    print(f'Fruta de índice {i}: {frutas[i]}.')
