def count_letter_a(string):
    count = string.lower().count('a')
    return f"A letra 'a' aparece {count} vezes na string."

# Exemplo de uso
string = input("Informe uma string: ")
print(count_letter_a(string))

