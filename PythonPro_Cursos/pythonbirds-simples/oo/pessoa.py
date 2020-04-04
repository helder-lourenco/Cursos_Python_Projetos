class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome
    def cumprimentar(self):
        return f'ola {id(self)}'
if __name__ == '__main__':
    p = Pessoa('Rogerio')
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Rogerio'
    print(p.nome)