# Faça um programa que leia uma lista de números e retorne a média dos números pares.

lista01 = []
lista02 = []
for i in range(0,10):
    num = int(input("insira um numero:"))
    lista01.append(num)

for i in range(0,len(lista01),2):
    lista02.append(lista01[i])
    print(lista02)

media = (lista02[0]+lista02[1]+lista02[2]+lista02[3]+lista02[4])//(len(lista02))
print(media)