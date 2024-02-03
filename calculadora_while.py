while True:
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair:
        break
        
    else:
        opcao = input('''Qual operação gostaria de realizar? 
                somar (+)
                subtrair (-)
                dividir (/)
                Escolha: ''')
        if opcao not in '+-/':
            print('Opção inválida')
            break

        
        while ValueError:
            try:
                valor1 = input('Digite o primeiro valor: ')
                valor_int1 = int(valor1)
                valor2 = input('Digite outro valor: ')
                valor_int2 = int(valor2)
                
            except ValueError:
                print('Voce não digitou um numero válido.')

            if opcao == '+':
                    somar = valor_int1 + valor_int2
                    print(somar)
            elif opcao == '-':
                subtrair = valor_int1 - valor_int2
                print(subtrair)
            elif opcao == '/':
                divisao = valor_int1 / valor_int2
                print(divisao)
            break

                            
