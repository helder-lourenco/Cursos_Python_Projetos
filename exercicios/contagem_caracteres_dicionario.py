def contar_caracteres_dicionario(s):

    resultado = {}

    for caracter in s:
        resultado[caracter]=resultado.get(caracter, 0) +1

    return resultado

if __name__ == '__main__':
   print(contar_caracteres_dicionario('rogerio'))
   print()
   print(contar_caracteres_dicionario('eliete'))