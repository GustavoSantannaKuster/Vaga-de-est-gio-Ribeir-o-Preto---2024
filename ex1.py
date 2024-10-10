def is_fibonacci(n):
    # Função para verificar se um número é quadrado perfeito
    def is_perfect_square(x):
        return int(x**0.5)**2 == x

    # Um número é Fibonacci se e somente se 5*n^2 + 4 ou 5*n^2 - 4 for um quadrado perfeito
    def is_fibonacci_number(n):
        return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

    if is_fibonacci_number(n):
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."

# Exemplo de uso
num = int(input("Informe um número: "))
print(is_fibonacci(num))

