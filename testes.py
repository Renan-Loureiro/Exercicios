# lista = [
#     valor
#     for valor in range(0,10)
#     ]


# iterator = iter(lista)
# for c in range(len(lista)):
#     print(next(iterator))

# import sys

# # Generator expression, Iterables e Iterators em Python
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable)  # tem __iter__ e __next__
# lista = [n for n in range(1000000)]
# generator = (n for n in range(1000000))

# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# print(next(generator)) #a cada iteração ele vai te dar um valor da lista.

# # for n in generator:
# #     print(n)


# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2 # Pausar
#     print('Mais uma...')
#     yield 3 #Pausar
#     print('Vou terminar...')

#     return 'ACABOU'

# gen = generator(n=0)


# for n in gen: #for está fazendo o papel do next() nesse generator
#     print(n)

# try:
#     a = 10
#     b = 0
#     c = a / b
# except ZeroDivisionError:
#     print('ERRO! NÃO É POSSÍVEL DIVIDIR POR ZERO.')

# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
# try:
#     print('ABRIR ARQUIVO')
#     8/0
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
#     print('DIVIDIU ZERO')
# except IndexError as error:
#     print('IndexError')
# except (NameError, ImportError):
#     print('NameError, ImportError')
# else:
#     print('Não deu erro')
# finally:
#     print('FECHAR ARQUIVO')

# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(platform)
# exit()