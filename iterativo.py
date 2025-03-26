def factorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = numero * factorial(numero - 1)
        print(f"factorial({numero}) = {resultado}")
        return resultado
print(factorial(5))