lista = ['Renan', 'Jana', 'Gi', 'Igor']
tamanho = range(len(lista))

for i in tamanho:
    print(f'indice da lista {i}')


#voce pode acessar o indice da lista utilicando a função enumerate. Ex.:
    
lista_enumerada = enumerate(lista)
print(lista_enumerada)