def contar_caracteres(s):

    caracteres_ordenados = sorted(s)

    caracteres_anteriores = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracteres_anteriores:
            contagem =1

        else:
            print(f'{caracteres_anteriores}: {contagem}')
            caracteres_anteriores = caracter
            contagem=1

    print(f'{caracteres_anteriores}:{contagem}')

if __name__ == '__main__':
    contar_caracteres('rogerio')
    print()
    contar_caracteres('eliete')