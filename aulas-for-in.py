# texto = 'William'
# tn = ''

# for l in texto:
#     tn += f'*{l}'
# print(tn)

## ----- For + Range ----- ##
# range -> range(start, stop, step)

# numeros = range(1, 10, 2)

# for n in numeros:
#     print(n)

# print(numeros)
"""
iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador 
"""
#texto = 'William' #iterável
#iteratador = iter(texto) #iterator

#while True:
#    try:
#        letra = next(iteratador)
#        print(letra)
#    except StopIteration:
#        break

#for letra in texto:
#    print(letra)

# for i in range(10):
#     if i == 2
#         print('i é 2...')
#         continue

#     if i == 5:
#         print('i é 8')
#         break
#     for j in range(1, 3):
#         print(i, j)
# else:
#     print('For completo')

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_certa = 'python'
letra_certa = ''
numero_tentativa = 0

while True:
    os.system('cls')
    letra_digitada = input('Digite apenas uma letra: ')
    numero_tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra_digitada in palavra_certa:
        letra_certa += letra_digitada
    
    palavra_formada = ''
    for letra in palavra_certa:
        if letra in letra_certa:
            palavra_formada += letra
        
        else:
            palavra_formada += '*'
    

    if palavra_formada == palavra_certa:
        os.system('cls')
        print(f'Você acertou a palavra certa: {palavra_certa}')
        print(f'Numero de tentativas: {numero_tentativa}')
        letra_certa = ''
        numero_tentativa = 0
