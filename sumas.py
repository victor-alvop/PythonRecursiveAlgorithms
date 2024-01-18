def suma(x,y):
    return x if y == 1 else x + suma(x, y-1)

resultado = suma(3,3)
print(f'Resultado: {resultado}')

