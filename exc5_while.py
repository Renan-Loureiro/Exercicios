nome = 'RENAN LOUREIRO'

tamanho_nome = len(nome)
contador = 0

while contador <= tamanho_nome:    
    print(f'{nome[contador]}*', end='')
    contador += 1
   
'''RESPOSTA DO PROFESSOR ABAIXO'''

"""
Iterando strings com while
"""



nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)