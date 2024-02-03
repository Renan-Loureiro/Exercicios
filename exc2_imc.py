def imc(peso=0, altura=0):
    val = peso / altura ** 2
    return val



altu = float(input('Qual sua altura? ' ))
pes = int(input('Qual seu peso? '))
calculo = imc(pes, altu)
print(f'Seu imc é: {calculo:.2f}')