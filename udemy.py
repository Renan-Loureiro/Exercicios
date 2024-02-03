
# #.strip() é para tirar os espaços depois e antes, rstrip tira os da direita e lstrip da esquerda
# #.join() une uma string

''''Desenpacotamento em chamadas de funções''' 
# # Desempacotamento em chamadas
# # de métodos e funções
# string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
# tupla = 'Python', 'é', 'legal'
# salas = [
#     # 0        1
#     ['Maria', 'Helena', ],  # 0
#     # 0
#     ['Elaine', ],  # 1
#     # 0       1       2
#     ['Luiz', 'João', 'Eduarda', ],  # 2
# ]

# # p, b, *_, ap, u = lista
# # print(p, u, ap)

# # print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# # print(*lista)
# # print(*string)
# # print(*tupla)

# print(*salas, sep='\n')


""" EXERCICIO 9
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#SEGUNDO DIGITO
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""