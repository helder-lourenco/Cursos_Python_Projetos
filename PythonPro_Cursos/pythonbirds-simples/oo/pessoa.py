class Pessoa:
    def __init__(self, nome=None, idade=35, *filhos):

        self.nome = nome
        self.idade=idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'ola {id(self)}'
if __name__ == '__main__':
    p=Pessoa('Rogerio')
    guilherme = Pessoa(nome='Guilherme')
    rogerio = Pessoa(guilherme, nome='Rogerio')
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Rogerio'
    print(p.nome)

    for filho in rogerio.filhos:
        print(filho.nome)