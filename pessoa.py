class Pessoa:
    def __init__(self, nome, idade, cor_olho):
        self.nome = nome
        self.idade = idade
        self.cor_olho = cor_olho
    def __repr__(self):
        return f'{self.nome}, {self.idade}, {self.cor_olho}'
    
  