import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

cpf = '43807336885'

nove_digitos = cpf[:9]

cont_regressivo1 = 10
resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * cont_regressivo1
    cont_regressivo1 -= 1
prim_digito = (resultado * 10) % 11
prim_digito = prim_digito if prim_digito <= 9 else 0


dez_digitos = nove_digitos + str(prim_digito)

contagem_regressiva2 = 11

resultado_2 = 0
for num in dez_digitos:
    resultado_2 += int(num) * contagem_regressiva2
    contagem_regressiva2 -= 1
seg_digito = (resultado_2 * 10) % 11
if seg_digito <= 9:
    seg_digito = seg_digito
else:
    seg_digito = 0

cpf_gerado = f'{nove_digitos}{prim_digito}{seg_digito}'

if cpf == cpf_gerado:
    print(f'CPF {cpf} é válido.')
else:
    print(f'CPF {cpf} é invlálido.')