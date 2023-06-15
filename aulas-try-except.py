numero_str = input('Digite um numero: ')

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('Float', numero_float)
    print(f'O numero digitado foi {numero_str}, e o dobro dele é {numero_float * 2}')
except:
    print('Você não digitou um numero')

#EM PYTHON HÁ UMA CONVENSÃO QUE DIZ QUE QUANDO FOR COLOCAR UMA VARIAVEL QUE NÃO IRÁ MUDAR, VOCÊ DEVE POR ELA EM CAIXA ALTA

velocidade = 65 #velocidade atual do carro
local_carro = 101 #km que o carro está

RADAR_1 = 60 #velocidade permitida
LOCAL_1 = 100 #km do radar
RADAR_RANGE = 1 #Distancia onde o radar pega

vel_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_pass_radar_1

if vel_pass_radar_1:
    print('Velo do carro que passou radar1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1 and vel_pass_radar_1:
    print('Carro Multado no radar 1')

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('foi feito algo')
else:
    print('Não feito algo')
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')

if numero .isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 ==0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {numero_int} é um numero Inteiro e é {par_impar_texto}')
else:
    print('Você não digitou um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
hora = input('Digite a hora do dia: ')
hora_int = int(hora)
if hora_int >= 18 and hora_int <= 23:
    pritn('Boa noite!')
elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde!')
elif hora_int >= 0 and hora_int <= 11:
    print('Bom dia!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')