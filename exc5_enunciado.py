
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# numero = int(input('Digite um numero: '))
# try:
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'O numero {numero} é par.')
#     else:
#         print(f'O numero {numero} é impar')
# except ValueError:
#     print(F'Voce não digitou um numero inteiro.')

# entrada = input('Digite um número: ')

# # if entrada.isdigit():
# #     entrada_int = int(entrada)
# #     par_impar = entrada_int % 2 == 0
# #     par_impar_texto = 'ímpar'

# #     if par_impar:
# #         par_impar_texto = 'par'

# #     print(f'O número {entrada_int} é {par_impar_texto}')
# # else:
# #     print('Você não digitou um número inteiro')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 218-23.

    


# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

# nome = input('Digite seu nome: ')
# tamanho_nome = len(nome)
# if tamanho_nome <= 4:
#     print('Seu nome é curto.')
# elif tamanho_nome <= 6:
#     print('Seu nome tem um tamanho normal')
# else:
#     print('Seu nome é grande.')