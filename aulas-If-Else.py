# entrada = input('Você quer "entrar" ou "sair"? ')

# if entrada == "entrar":
#     print('Você entrou no sistema')
# elif entrada == "sair":
#     print('Você saiu do sistema')
# else:
#     print('Você não digitou nada')

# idade = input('Digite sua idade ')
# maioridade = 18
# int_idade = int(idade)

# if int_idade > maioridade:
#     print(f'Você tem {int_idade}, e é de maior')
# elif int_idade == maioridade:
#     print(f'Você tem {int_idade}, e acaboud e se tornar maior de idade')
# else:
#     print(f'Você tem {int_idade}e é de menor')

# entrada = input('[E]ntrar ou [S]air?')
# senhada_digitada = input('Digite sua senha: ')
# senha_permitida = '123456'

# if (entrada =='E' or entrada == 'e') and senhada_digitada == senha_permitida:
#     print('Você entrou no sistema')
# elif entrada == 'E' and senhada_digitada != senha_permitida:
#     print('Você digitou a senha incorreta')
# else:
#     print('Você saiu do sistema')


# senha = input('Digite sua senha: ')

# if not senha:
#     print('Você não digitou nada')
# else:

# if 0 and 1:
#     print(true and 1)

# nome = "william"
# encontrar = 'l'
# if encontrar in nome:
#     print(f'{encontrar} aparece em {nome}')
# else:
    # print(f'{encontrar} não aparece em {nome}')
# print('w' in nome)
# print('ll' not in nome)

#INTERPOLAÇÃO DE STRINGS
#s - Str
#d , i - Int
#f - float
# #x, X - Hexadecimal (ABCDEF0123456789)
# nome = 'William'
# preco = 550.51124
# gasto = '%s, gastou um total de R$%.2f' %(nome, preco)

# print(gasto)

# print('O Hexadecimal de %d é %04x' % (20, 15)) #pode ser x ou X e a casa decimal pode ser 4 ou 8 (mais usado comumente)

"""
Formatação básica de strings f-strings
s - str
d - int
f - float
.2f 2 seria a casa decimal
x ou X - Hexadecimal
> - Preencher a esquerda
< - Preencher a direita
# ^ - Centro
# Conversion flags - !r !s !a
# """
# a = 'ABC'
# b = -1201.1215484689
# print(a)
# print(f'{a:>10}')
# print(f'{a:^10}')
# print(f'{a:#^11}')
# print(f'{b:-,.2f}')
# # print(f'O hexadecimald de 1500 é {1500:08x}')

# var = 'william sierro'
# print(len(var[0:14:3]))
# print(var[0:14:3])
# print(var[::2])

# nome = input('Digite seu nome: ')
# idade = input('Digite sua idade: ')

# if nome != '' and idade != '':
#     print(f'Seu nome é {nome}, e sua idade é {idade}')
#     print(f'Seu nome invertido é {nome[::-1]}')
#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]} e a ultima é {nome[-1]}')
#     if ' ' in nome:
#         print('Seu nome contém espaço')
#     else:
#         print('Seu nome não contém espaço')
# else:
    # print('Desculpe você não digitou ou seu nome, ou sua idade')
