numero = 0

while numero < 10:
    numero += 1
   
    
    if numero == 4:
        continue  
    if numero == 8:
        print(numero)
        break
    
    print(numero)

qtd_linha = 5
qtd_coluna = 5
linha = 1

while linha <= qtd_linha:
    
    coluna = 1
    while coluna <= qtd_coluna:
        print(linha, coluna)
        coluna += 1
    linha += 1
print('Acabou')

nome = 'William Sierro'

i = 0
novo_nome = ''
while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1 
print(novo_nome)

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador que deseja(+-*/): ')
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos numeros é invalido')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
   
    if operador == '+':
        print(f'{num1_float}+{num2_float}=', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float}-{num2_float}=', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float}*{num2_float}=', num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float}/{num2_float}=', num1_float / num2_float)


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

    print(sair)

# # ----- While / else ----- #
string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado')

print('Fora do while')

# ----- While Treino ----- #

frase = 'O python é uma linguagem de programação'\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum.'

# print(frase.count())

i = 0
qtd_apamais = 0
letra_apamais = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == " ":
        i += 1
        continue
    
    xletrasap = frase.count(letra_atual)

    if qtd_apamais < xletrasap:
        qtd_apamais = xletrasap
        letra_apamais = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi: "{letra_apamais}" '\
    f'E ela apareceu: {qtd_apamais} vezes')      