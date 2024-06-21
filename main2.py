from pessoa import Pessoa

pessoa1 = Pessoa('Ze', 45,'Castanho')
pessoa2 = Pessoa('Chico', 37, 'Verde')
pessoa3 = Pessoa('Paty', 20, 'Azul')

def salva_pessoa(pessoa):
    with open('pessoa.txt', 'a') as file:
        file.write(f'Pessoa: nome {pessoa.nome}; idade{pessoa.idade}; cor_olho {pessoa.cor_olho}\n')

def salva_lista_pessoa(list_p:list[Pessoa]):
    with open('pessoa.txt', 'a') as file:
        for pessoa in list_p:
            salva_pessoa(pessoa)

def le_lista_pessoa():
    list_p = []
    with open('pessoa.txt','r') as file:
        lines = file.readlines()
    for line in lines:
        if line.starswith('Pessoa: '):
            atributos = line.strip().split('Pessoa= ')[1]
            nome = atributos.split(':')[1].split(',')[0]
            idade = atributos.split(':')[2].split(',')[0]
            cor_olho = atributos.split(':')[3]
            pessoa = Pessoa(nome, idade, cor_olho)
            list_p.append(pessoa)
            return list_p

list_pessoa = [pessoa1, pessoa2, pessoa3]
salva_lista_pessoa
salva_pessoa(pessoa1)
salva_pessoa(pessoa2)
salva_pessoa(pessoa3)