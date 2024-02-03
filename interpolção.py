# Interpolação básica de strings

# s - string 
# d e i - int 
# f - float
# x e X - para hexadecimal


nome =  'Renan'
preco = 100.23
variavel = '%s, o preço é de %.2f ' %(nome, preco)
print(variavel)
print(10 * '-')
hexa = 'O preço %d em hexadecimal é %08X' %(15, 15)
print(hexa)