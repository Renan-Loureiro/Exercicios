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
from os import system

secreta = 'soldador'

print(f'{'-'*5}COMEÇANDO O JOGO{'-'*5}')
print(f'Descubra a palavra digitada. É uma profissão.')
letra_digitada = ''
cont = 0

while True:
    letra = input('Digite apenas uma letra: ')
    tamanho = len(letra)
    cont += 1

    if tamanho > 1:
        print('ERRO! Voce digitou mais de uma letra.')
        continue

    elif tamanho == 0:
        print('ERRO! Voce deixou o campo em branco.')
        continue
    
    if letra in secreta:
        letra_digitada += letra
    
    palavra_formada = ''

    for letra_secreta in secreta:
        if letra_secreta in letra_digitada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'
    print(palavra_formada)
    if palavra_formada == secreta:
        system('cls')
        print(f'Voce acertou! A palavra é {secreta}')
        print(f'Foram efetuadas {cont} tentativas.')
        cont = 0
        letra_digitada = ''