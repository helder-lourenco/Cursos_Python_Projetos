class Pessoa:
    olhos =2

    def __init__(self, *filhos, nome=None, idade=35):

        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'ola {id(self)}'
if __name__ == '__main__':
    guilherme = Pessoa(nome='Guilherme')
    rogerio = Pessoa(guilherme, nome='Rogerio')
    print(id(rogerio))
    print(Pessoa.cumprimentar(rogerio))
    print(rogerio.cumprimentar())
    print(rogerio.nome)
    rogerio.nome = 'Rogerio'
    print(rogerio.nome)

    for filho in rogerio.filhos:
        print(filho.nome)

   