def sumatoria(valor):
    return 1 if valor == 1 else valor + (sumatoria(valor-1))

resultado = sumatoria(5)
print(f'Resultado: {resultado}')

