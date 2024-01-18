def potencia(x,y):
    return x if y == 1 else x * potencia(x, y-1)

resultado = potencia(3,4)
print(f'Resultado: {resultado}')

