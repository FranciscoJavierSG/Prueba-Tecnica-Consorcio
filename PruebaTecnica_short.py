def generate_possible_words(pattern):
    # Se crea una lista con una cadena vacía (para asegurar que al menos tengamos una palabra en la lista)
    possible_words = [''] 

    i = 0
    while i < len(pattern):
        if pattern[i] == '(': 

            #Se busca el índice del paréntesis de cierre correspondiente
            j = pattern.index(')', i)

            #Se obtienen los caracteres dentro de los paréntesis (opciones de posibles palabras). Desde el primer caracter (i+1) hasta el paréntesis de cierre (que no se cuenta)
            options = pattern[i+1:j]

            new_possible_words = []
            for word in possible_words: 
                for option in options: 
                    #Se agrega una nueva palabra formada al concatenar la letra actual (option) con cada letra posible (options)
                    new_possible_words.append(word + option)

            # Se actualiza la lista de palabras posibles
            possible_words = new_possible_words
            i = j + 1 
        else:
            # Si la letra (o carácter) actual no es un paréntesis de apertura, simplemente se agrega a cada palabra posible
            possible_words = [word + pattern[i] for word in possible_words]
            i += 1

    return possible_words

def count_matching_words(pattern, known_words):
    # Genera todas las posibles palabras que coinciden con el patrón dado
    possible_words = generate_possible_words(pattern)

    # Cuenta cuántas palabras en la lista 'known_words' coinciden con las posibles palabras generadas a partir del 'pattern' dado utilizando una expresión generadora y la función sum()
    count = sum(word in known_words for word in possible_words)

    return count

if __name__ == "__main__":
    # L es el largo de las palabras en el idioma alienígena
    # D es el número de palabras conocidas en el idioma alienígena
    # N es la cantidad de casos de prueba
    L, D, N = map(int, input().split())
    known_words = [input() for _ in range(D)] # Se agregan las palabras conocidas a la lista known_words

    # Procesamiento de los casos de prueba
    for case in range(1, N+1):
        pattern = input()

        # Se usa la función count_matching_words para contar las palabras que tienen el patrón 'pattern' y las compara con las palabras conocidas 'known_words'
        matching_words = count_matching_words(pattern, known_words)

        # La palabra que se imprime es "Case" (en inglés) y no "Caso" (en español) porque así lo requería el enunciado
        print(f"Case #{case}: {matching_words}\n")