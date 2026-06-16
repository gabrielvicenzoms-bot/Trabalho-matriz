editar = input ('você deseja editar a lista de filme?(digite apenas "sim" se deseja editar)')
while editar == 'sim':
    filmes = [
        ['Matrix', 1999, 8.5],
        ['Avatar', 2009, 7.9],
        ['Interestelar', 2014, 8.7],
        ['Vingadores', 2012 , 8.0],
        ['Sonic', 2020, 6.5],
        ['Jumanji', 1995, 7.1]
    ]

    adicionar  = input('você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme)')
    while adicionar == 'sim':
        novofilme = input('insira o novo filme')
        ano = input('o ano que lançou')
        nota = float(input('insira a nota do filme'))
        filmes.append([novofilme, ano, nota])
        adicionar  = input('você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme)')


    remover  = input('você deseja remover um novo filme?(digite apenas "sim" se deseja remover um filme)')
    while remover == 'sim':
        removido = input('insira o nome do filme que deseja remover')
        for f in filmes:
            if f[0] == removido:
                filmes.remove(f)
        remover  = input('você deseja remover um novo filme?(digite apenas "sim" se deseja remover um filme)')



    with open ('arquivo.txt','w') as arquivo:
        for i in filmes:
            arquivo.write(f"{i}\n")


    with open("arquivo.txt", "r") as arquivo:
        ler = arquivo.read()
        print (ler)

    editar = input ('você deseja editar a lista de filme?(digite apenas "sim" se deseja editar)')
