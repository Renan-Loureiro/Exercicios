# #Formatação básica de strings
# s - string 
# d - int 
# f - float 
# .<numero de digitos>f 
# x ou X - hexadecimal
# (Caractere)(><^)(Quantidade)
# > - esquerda
# < - direita
# ^ - centro 
# Sinal - + ou - 
# Ex.: 0>-100, .1f
# Conversion flags - !r !s !a

variavel = 'ABCD'
print(f'{variavel:->10}') #ALINHAR A ESQUERDA
print(f'{variavel:-<10}') #ALINHAR A DIREITA
print(f'{variavel:-^10}')#CENTRALIAR TEXTO
print(f'{variavel}')
print(f'O hexadecimal de 1500 é {1500:08X}') #TRANSFORMANDO EM HEXADECIMAL



