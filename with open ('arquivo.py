#Programa para adicionar um filme, ano que lançou e nota em um arquivo .txt

filmes = [
    ["Matrix", 1999, 8.5],
    ["Avatar", 2009, 7.9],
    ["Interestelar", 2014, 8.7]
]

adicionar  = input('você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme)')
while adicionar == 'sim':
    novofilme = input('insira o novo filme')
    ano = input('o ano que lançou')
    nota = float(input('insira a nota do filme'))
    filmes.append([novofilme, ano, nota])
    adicionar  = input('você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme)')

with open ('arquivo.txt','w') as arquivo:
    for i in filmes:
        arquivo.write(f"{i}\n")
