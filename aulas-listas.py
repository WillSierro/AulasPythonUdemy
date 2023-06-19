"""
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
metodos uteis: 
    append - Adiciona item no final da lista,
    insert - Adiciona item no indice escolhido,
    pop - Remove item  no final da lista,
    del - apaga um indice,
    clear - limpa a lista,
    extend - estende a lista,
    + - concatena listas
Create Read Update --- Delete
Criar, ler, alterar, apagar = lista[1] (CRUD)

"""

#.......01234
#.......54321
string = 'ABCDE' #5 caracteres

lista = [1, 'William', 'Henrique', 'Espicaski', 'Sierro', '14061990', True]
lista[-2] = '14/06/1990'

print(lista)
print(lista[1].upper())

lista2 = [10, 20, 30, 40]
nume = lista[2]
print(lista2)
del lista2[1]
print(nume)
print(lista2)
lista2.append(50)
print(lista2)
lista2.pop()
lista2.append(60)
print(lista2)
lista2.pop(1)
lista2.append(70)
print(lista2)
lista2.insert(0, 5)
print(lista2)
print('lista Não Apagada')
#lista2.clear()
print(lista2)
print('lista Apagada')

lista3 = lista + lista2
print(lista3)
lista4 = lista.extend(lista2)
print(lista4)
lista.extend(lista2)
print(lista)

#lista5 = lista
lista5 = lista.copy()
lista[0] = '01'
print(lista)
print(lista5)

import os

os.system('cls') ########## -- para ver este tema comente esta linha -- ##########

nova_lista = ['William', 'Henrique', 'Espicaski', 'Sierro', '14061990']
indices = range(len(nova_lista))

for indice in indices:
    print(indice, nova_lista[indice])


os.system('cls') ########## -- para ver este tema comente esta linha -- ##########
"""
########## -- Tuplas -- ########## '' ou ()
"""
nomes1 = 'William', 'Henrique', 'Espicaski', 'Sierro', '14061990'
_, nLista, *_ = ['William', 'Henrique', 'Espicaski', 'Sierro', '14061990']
print(nLista)
print(nomes1)

os.system('cls')########## -- para ver este tema comente esta linha -- ##########
"""
########## -- Enumerate -- ##########
"""

nomes = ['William', 'Henrique', 'Espicaski', 'Sierro', '14061990']
nnomes = enumerate(nomes)

for i, nome in enumerate(nomes):
    print(i, nome)

os.system('cls') ########## -- para ver este tema comente esta linha -- ##########
"""
########## -- Exercicio -- ##########
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""
#lista_compras = []
#novLista = input('Você deseja [a]Adicionar, [b]Apagar ou [l]Listar? ')

#if novLista == 'a':
#    lista_compras.append(input('Digite um item para a Lista: '))
    
#elif novLista == 'b':
#    lista_compras.remove(input('Digite o indice ao qual deseja remover: '))
#elif novLista == 'l':
#    for i, item in enumerate(lista_compras):
#        print(i, item)
#else:
#    print('Você não escolheu o que quer fazer!')
lista_compras = []
while True:
    print('Selecione uma opção:')
    opcao = input('[a]Adicionar, [b]Apagar ou [l]Listar: ')

    if opcao == 'a':
        item = input('Digite o Item: ')
        lista_compras.append(item)
    elif opcao == 'b':
        apagar = input('Digite o indice a ser apagado: ')
        try:
            apaga = int(apagar)
            del lista_compras[apaga]
        except ValueError:
            print('Digite o numero do indice (Nº Inteiro)')
        except IndexError:
            print('Indice não existe')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l': 
        if len(lista_compras) == 0:
            print('Não tem itens')
        for i, item in enumerate(lista_compras):
            print(i, item)
    else:
        print('Você não escolheu o que quer fazer!')


