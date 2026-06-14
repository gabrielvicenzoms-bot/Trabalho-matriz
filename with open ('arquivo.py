lista = [
    ['joao', 98, 1.70],
    ['victor', 18, 2.00],
    ['gabriel', 75, 1.70],
]


aluno =['luis',67,3.07]
lista.append(aluno)

with open ('arquivo.txt','w') as arquivo
    for i in lista:
        arquivo.write(f"{i}\n")
