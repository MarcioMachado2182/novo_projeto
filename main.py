
atributos = ''
with open("pessoas.txt",'r') as file:
    lines = file.readlines()
for line in lines:
    if line.startswith('Pessoa= '):
        atributos = line.strip().split('Pessoa= ')[1]

print(atributos)
