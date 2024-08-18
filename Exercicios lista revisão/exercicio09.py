# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

lista = ["Jon", "Martha", "Allen", "Damian", "Richard", "Jason", "Tim", "Alfred"]
nomesA = []

for nome in lista:
    if nome[0] == "A":
        nomesA.append(nome)
print(nomesA)
