import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

def multiplicar(*arg):
    total = 1
    for num in arg:
        total *= num
    return total


def impar(x):
    multiplo_de_dois = x % 2 == 0
    if multiplo_de_dois:
        return f'O numero {x} é par'
    return f'O numero {x} é impar'
    


resultado = multiplicar(3, 3)

print(resultado)
print(impar(resultado))