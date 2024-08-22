# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
# programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
# computador e determinar o vencedor.

import random

possibilidades = [0,1,2]
possibilidadesStrings = ["Pedra","Papel","Tesoura"]

#jogadaPlayer = int(input("Digite o número equivalente à sua jogada: \n Pedra[0], Papel[1], Tesoura[2]"))
#jogadaPlayerString = possibilidadesStrings[jogadaPlayer]



repetir = False

jogar = input("Deseja jogar? [S/N]")
if jogar == 'n':
    repetir = True
elif jogar == 'n':
    repetir = False
else: 
    repetir = True

while repetir == True:

    jogadaPlayer = int(input("Digite o número equivalente à sua jogada: \n Pedra[0], Papel[1], Tesoura[2]"))
    jogadaPlayerString = possibilidadesStrings[jogadaPlayer]

    jogadaMaquina = random.choice(possibilidades)
    jogadaMaquinaString = possibilidadesStrings[jogadaMaquina-1]

    if jogadaPlayer <=2:

        if (jogadaPlayer+1) % 3 == jogadaMaquina:
            print("Sua jogada:",jogadaPlayerString)
            print("Jogada da máquina:",jogadaMaquinaString)
            print(jogadaMaquinaString,"ganha de",jogadaPlayerString,"você perdeu!")
            
            #break

        elif jogadaPlayer == jogadaMaquina:
            print("Sua jogada:",jogadaPlayerString)
            print("Jogada da máquina:",jogadaMaquinaString)
            print("Empate!")
            
            #break

        else:
            print("Sua jogada:",jogadaPlayerString)
            print("Jogada da máquina:",jogadaMaquinaString)
            print(jogadaPlayerString,"ganha de",jogadaMaquinaString,"você ganhou!")
            
            #break

    else:
        print("Jogada Inválida!")
        
        #break



    pergunta = input(("Deseja continuar? [S/N]"))
    if pergunta == 'n':
        repetir = True
    elif pergunta == 'n':
        repetir = False
    else: 
        repetir = True


