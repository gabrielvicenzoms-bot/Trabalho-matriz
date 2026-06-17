# Lista composta contendo os filmes e suas informações:
# [nome do filme, ano de lançamento, nota]
filmes = [
    ['Matrix', 1999, 8.5],
    ['Avatar', 2009, 7.9],
    ['Interestelar', 2014, 8.7],
    ['Vingadores', 2012 , 8.0],
    ['Sonic', 2020, 6.5],
    ['Jumanji', 1995, 7.1]
]

# Pergunta ao usuário se deseja iniciar a manipulação dos dados
editar = input('Você deseja editar a lista de filme?(digite apenas "sim" se deseja editar) ')


while editar == 'sim':
   
    print("Lista atual de filmes:")
    # Percorrer a matriz
    for f in filmes:
        print(f)



    adicionar = input('Você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme) ')


    while adicionar == 'sim':

        novofilme = input('Insira o novo filme: ')

        ano = int(input('O ano que lançou: '))

        nota = float(input('Insira a nota do filme: '))

        # Adiciona um novo filme no final da lista composta
        filmes.append([novofilme, ano, nota])

        for f in filmes:
         print(f)

        adicionar = input('Você deseja adicionar um novo filme?(digite apenas "sim" se deseja adicionar um novo filme) ')



    remover = input('Você deseja remover um novo filme?(digite apenas "sim" se deseja remover um filme) ')


    while remover == 'sim':
        for f in filmes:
         print(f)

        removido = input('Insira o nome do filme que deseja remover: ')
        

        # Percorre a lista procurando o filme informado pelo usuário
        for f in filmes[:]:
        
            # Verifica se o nome do filme é igual ao escolhido
            if f[0] == removido:
                
                # Remove o filme encontrado da matriz
                filmes.remove(f)


        remover = input('Você deseja remover outro filme?(digite apenas "sim" se deseja remover um filme) ')



    atualizar = input('Deseja editar a nota um flime?(digite apenas "sim" se deseja editar um filme)  ')


    while atualizar == "sim":
        for f in filmes:
         print(f)

        filme_atualizar = input("Digite o filme: ")

        # Procura o filme que será atualizado
        for f in filmes:

             
            # Confere o nome do filme
            if f[0] == filme_atualizar:
                
                # Atualiza a nota (posição 2 da lista interna)
                f[2] = float(input("Digite a nova nota: "))
            
                    


        atualizar = input('Deseja atualizar outro? ')


    # Abre o arquivo no modo escrita
    # Caso exista conteúdo antigo, ele será substituído
    with open('arquivo.txt','w') as arquivo:

        # Percorre cada filme da matriz
        for i in filmes:

            # Salva nome, ano e nota separados por ponto e vírgula
            arquivo.write(f"{i[0]};{i[1]};{i[2]}\n")


    # Abre o arquivo no modo leitura
    with open("arquivo.txt", "r") as arquivo:

        # Lê todas as informações armazenadas no arquivo
        ler = arquivo.read()

        # Exibe os dados na tela
        print(ler)

    # Cria uma nova lista para armazenar os dados recuperados
    nova_lista = []

    # Abre o arquivo para leitura
    with open("arquivo.txt", "r") as arquivo:

       # Percorre cada linha do arquivo
        for linha in arquivo:

            # Remove espaços e separa os dados pelo ;
            dados = linha.strip().split(";")

            # Reconstrói a lista do filme convertendo os tipos de dados
            nova_lista.append([
                dados[0],
                int(dados[1]),
                float(dados[2])
            ])

    # Substitui a lista antiga pela lista recuperada do arquivo
    filmes = nova_lista
    print("Lista recuperada do arquivo TXT:")
    
    for f in filmes:
        print(f)

    editar = input('Você deseja editar a lista de filme?(digite apenas "sim" se deseja editar) ')


print("Programa encerrado.")
