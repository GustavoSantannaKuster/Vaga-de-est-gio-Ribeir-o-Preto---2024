def inverter_string(s):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Itera pelos caracteres da string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        # Adiciona cada caractere à string invertida
        string_invertida += s[i]

    # Retorna a string invertida
    return string_invertida


# Teste da função com uma string específica
string_original = "Python"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
