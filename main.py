from pessoa import Pessoa

def le_pessoa():
    with open("pessoa.txt",'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Pessoa= '):
            atributos = line.strip().split('Pessoa= ')[1]
            nome = atributos.split(':')[1].split(',')[0]
            idade = atributos.split(':')[2].split(',')[0]
            cor_olho = atributos.split(':')[3]
            pessoa1 = Pessoa(nome,idade,cor_olho)
            return pessoa1
pessoa = le_pessoa()        




