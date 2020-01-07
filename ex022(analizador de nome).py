nome = str(input('digite o seu nome completo:')).strip()
print('Letras maiúsculas: {}'.format(nome.upper()))
print('Letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} espaços'.format(len(nome.split())-1))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))#conta contas palavras tem e tira a quantidade de espaços
div = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(div[0])))#printa a palavra 0 e conta quantas letras ela tem
#print(nome.find(' '))