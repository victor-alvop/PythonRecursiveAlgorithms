# (m-n,n + 1)

def division(m,n):  
    return 1 if m == n else division(m-n,n)+1

resultado = division(20,5)
print(f'Resultado: {resultado}')