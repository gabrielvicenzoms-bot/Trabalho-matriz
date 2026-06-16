filmes = [
    ['Matrix', 1999, 8.5],
    ['Avatar', 2009, 7.9],
    ['Interestelar', 2014, 8.7],
    ['Vingadores', 2012 , 8.0],
    ['Sonic', 2020, 6.5],
    ['Jumanji', 1995, 7.1]
]


editar = input('Você deseja editar a lista de filme?(digite apenas "sim" se deseja editar) ')


while editar == 'sim':

    # Percorrer a matriz

    for f in filmes:
        print(f)



    adicionar = input('Você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme) ')


    while adicionar == 'sim':

        novofilme = input('Insira o novo filme: ')

        ano = int(input('O ano que lançou: '))

        nota = float(input('Insira a nota do filme: '))


        filmes.append([novofilme, ano, nota])


        adicionar = input('Você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme) ')



    remover = input('Você deseja remover um novo filme?(digite apenas "sim" se deseja remover um filme) ')


    while remover == 'sim':

        removido = input('Insira o nome do filme que deseja remover: ')


        for f in filmes:

            if f[0] == removido:

                filmes.remove(f)


        remover = input('Você deseja remover outro filme?(digite apenas "sim" se deseja remover um filme) ')



    atualizar = input('Deseja atualizar um filme? ')


    while atualizar == "sim":

        filme_atualizar = input("Digite o filme: ")


        for f in filmes:

            if f[0] == filme_atualizar:

                f[2] = float(input("Digite a nova nota: "))


        atualizar = input('Deseja atualizar outro? ')



    with open('arquivo.txt','w') as arquivo:

        for i in filmes:

            arquivo.write(f"{i[0]};{i[1]};{i[2]}\n")



    with open("arquivo.txt", "r") as arquivo:

        ler = arquivo.read()

        print(ler)



    nova_lista = []


    with open("arquivo.txt", "r") as arquivo:


        for linha in arquivo:

            dados = linha.strip().split(";")

            nova_lista.append([
                dados[0],
                int(dados[1]),
                float(dados[2])
            ])


    filmes = nova_lista


    editar = input('Você deseja editar a lista de filme?(digite apenas "sim" se deseja editar) ')



print("Programa encerrado.")
