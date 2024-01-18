def multiplicacion(m,n):
    return m if n == 1 else  m + multiplicacion(m,n-1)

def potencia(x,y):
    return 1 if y == 0 else multiplicacion(x,potencia(x,y-1))


print(multiplicacion(5,4))

w= 
print(w.reverse())