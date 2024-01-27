import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

#Função que recebe as perguntas e as opcões. (inserir as opcões como listas.)
def perguntas(txt, opcoes):
    print(txt)
    print('Opções:')
    for indice, valor in enumerate(opcoes):
        print(f'{indice}) {valor}')
    while True:
        try:
            resposta = input('Escolha uma opção: ')
            resposta_int = int(resposta)    
        except ValueError:
            print('Digite apenas numero')
            continue
        else:
            break
    return resposta_int

                
    # Programa com validação.
while True:
    acertos = 0
    
    resposta_1 = perguntas('Quanto é 2 + 2?', ['1', '3', '4', '5'])
    if resposta_1 == 2:
        print('Voce acertou!')
        acertos += 1
    else:
        print('Voce Errou!')
    
    resposta_2 = perguntas('Quanto é 5 x 5?', ['25', '55', '10', '51'])
    if resposta_2 == 0:
        print('Voce acertou!')
        acertos += 1
    else:
        print('Voce Errou!')

    resposta_3 = perguntas('Quanto é 10 ÷ 2', ['4', '5', '2', '1'])
    if resposta_3 == 1:
        print('Voce acertou!')
        acertos += 1
    else:
        print('Voce Errou!')
        break

print(f'Voce acertou {acertos} de 3 perguntas.')
