def verifica_fibonacci(numero):
    # Iniciando os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1

    # Verifica se o número é igual a um dos dois primeiros números da sequência
    if numero == a or numero == b:
        return True

    # Calcula a sequência de Fibonacci até que o próximo número seja maior que o número informado
    while b < numero:
        a, b = b, a + b

        # Se o próximo número na sequência for igual ao número informado, retorna True
        if b == numero:
            return True

    # Se o número informado não pertence à sequência de Fibonacci, retorna False
    return False


# Número a ser verificado se pertence à sequência de Fibonacci
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
