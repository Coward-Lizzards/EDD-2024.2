#Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

userInput = int(input("Insira um numero inteiro positivo"))
fatorial = 1

for i in range(1,userInput+1):
    fatorial = fatorial * i

print("O fatorial de",userInput,"é:",fatorial)