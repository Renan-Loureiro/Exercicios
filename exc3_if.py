valor_1 = input('Digite um valor: ')
valor_2 = input('Digite um outro valor: ')

var1 = int(valor_1)
var2 = int(valor_2)

if var1 > var2:
    print(f'O primeiro valor {var1} é maior que o segundo valor {var2}')
elif var1 < var2:
    print(f'O segundo valor {var2} é maior que o primeiro valor {var1}')
else:
    print('Os valores digitados são iguais.')
