# Faça um programa que determine se um número é primo ou não.
num = int(input("Insira um número:"))

if num > 1 :
    for i in range(2, (num//2)+1):
        if (num%i) == 0:
            print(num,"não é um número primo.")
            break
    else:
        print(num,"é um número primo!")
else:
    print(num,"não é um número primo.")
