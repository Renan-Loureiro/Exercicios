import os

os.system('cls')

lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]serir [a]pagar [l]istar [s]air: ')
    if opcao == 'i':
        os.system('cls')
        lista.append(input('Valor: '))        
    elif opcao == 'a':
        elemento = input('Escolha o indice para apagar: ')
        try:
            elemento = int(elemento)
            del lista[elemento]
        except ValueError:
            print('ERRO! Digite um numerio int.')
        except IndexError:
            print('Indice não existe na lista.')
    elif opcao == 'l':
        for indice, nome in enumerate(lista):
            print(indice, nome)
    elif opcao == 's':
        print('Sua lista ficou final ficou.')
        for indice, nome in enumerate(lista):
            print(indice, nome)
        break
    else:
        print('Opção inválida. Digite apenas i, a, l ou s')