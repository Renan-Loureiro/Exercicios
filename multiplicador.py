import os

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

def criar_multiplicador(valor):
    def multiplicar(num):
        return valor * num
    return multiplicar


multiplicador = criar_multiplicador(2)

triplicar = criar_multiplicador(10)

print(multiplicador(2))
print(triplicar(3))