
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
#quando colocado o nomme da variavel junto ao = ele vai me mostrar o nome da variavel e o valor dela
#I igual a linha e a coluna que está dentro da fstring.
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha = } {coluna = }')
        coluna += 1
    linha += 1


print('Acabou')