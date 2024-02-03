"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ').upper()
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}.')
else:
    print('Desculpe, você deixou campos vazios.')

espaço = ' '
print(f'Seu nome invertido é {nome[::-1]}')
if espaço in nome:
    print(f'Seu nome contém {len(espaço)} espaços.')
    tamanho = len(nome) - len(espaço)
    print(f'Seu nome contém {tamanho} letras.')
else:
    print(f'Seu nome não contém espaços.')
    print(f'Seu nome contém {len(nome)}')

print(f'A primeira letra dos eu nome é {nome[0]} e a ultima {nome[-1]}')


