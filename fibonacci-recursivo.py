def fibonacci_recursivo(n, depth=0):
    print(" " * depth + f"Calculando fibonacci({n})")
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1, depth + 1) + fibonacci_recursivo(n - 2, depth + 1)

# Ejemplo de uso
if __name__ == "__main__":
    numero = int(input("Introduce el número para calcular Fibonacci: "))
    resultado = fibonacci_recursivo(numero)
    print(f"El resultado de fibonacci({numero}) es: {resultado}")