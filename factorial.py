def factorial(numero):
  return 1 if numero == 1 else numero * factorial(numero - 1)

resultado = factorial(5)
print(f'factorial: {resultado}')


