VOCALES = "aeiouáéíóúü"

def contar_vocales(frase: str) -> int:
    """
    Cuenta el número de vocales (incluyendo acentuadas) en una frase.

    :param frase: la frase para contar
    :return: el número de vocales
    """
    contador_vocales = 0

    frase = frase.lower()
    for caracter in frase:
        if caracter in VOCALES:
            contador_vocales += 1

    return contador_vocales



def contar_palabras(frase: str) -> int:
    """
    Cuenta el número de palabras en una frase.

    :param frase: la frase para contar
    :return: el número de palabras
    """
    return len(frase.split())


def analizar_frase(frase: str) -> tuple[int, int]:
    """
    Analiza el número de vocales y de palabras de una frase completa.

    :param frase: la frase a analizar
    :return: una tupla con el número de vocales y de palabras, respectivamente
    """

    return contar_vocales(frase), contar_palabras(frase)


def main():
    frase: str = input()

    vocales, palabras = analizar_frase(frase)

    # Salida
    print(f"\nVocales: {vocales} \nPalabras: {palabras}")


if __name__ == "__main__":
    main()