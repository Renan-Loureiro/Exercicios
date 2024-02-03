# Exercício
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
#######################################################################
import os
from mods_exc100 import aumento
import copy
os.system('cls')

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
    ]   

copia_produtos = copy.deepcopy(produtos)


for produto in copia_produtos:
    produto['preco'] = aumento(produto['preco'])
    

# print(*copia_produtos, sep='\n')
# print()

ordenados_nome = sorted(copy.deepcopy(copia_produtos), 
                        key=lambda p: p['nome'],
                        )

print(*ordenados_nome, sep='\n')
print()


ordenados_nome_reverse = sorted(copy.deepcopy(copia_produtos), 
                        key=lambda p: p['nome'],
                        reverse=True
                        )

print(*ordenados_nome_reverse, sep='\n')
print()


ordenados_preco = sorted(copy.deepcopy(copia_produtos), 
                        key=lambda p: p['preco'],
                        )

print(*ordenados_nome, sep='\n')
print()


ordenados_preco_reverse = sorted(copy.deepcopy(copia_produtos), 
                        key=lambda p: p['preco'],
                        reverse=True
                        )

print(*ordenados_preco_reverse, sep='\n')
print()
