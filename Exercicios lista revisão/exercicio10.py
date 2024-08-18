# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
# programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
# computador e determinar o vencedor.

import random

possibilidades = [1,2,3]
possibilidadesStrings = ["Pedra","Papel","Tesoura"]

jogadaPlayer = int(input("Digite o número equivalente à sua jogada: \n Pedra[1], Papel[2], Tesoura[3]"))
jogadaPlayerString = possibilidadesStrings[jogadaPlayer-1]

jogadaMaquina = random.choice(possibilidades)
jogadaMaquinaString = possibilidadesStrings[jogadaMaquina-1]

if (jogadaPlayer+1) % 3 == jogadaMaquina:
    print("Sua jogada:",jogadaPlayerString)
    print("Jogada da máquina:",jogadaMaquinaString)
    print(jogadaMaquinaString,"ganha de",jogadaPlayerString,"você perdeu!")
elif jogadaPlayer == jogadaMaquina:
    print("Sua jogada:",jogadaPlayerString)
    print("Jogada da máquina:",jogadaMaquinaString)
    print("Empate!")
else:
    print("Sua jogada:",jogadaPlayerString)
    print("Jogada da máquina:",jogadaMaquinaString)
    print(jogadaPlayerString,"ganha de",jogadaMaquinaString,"você ganhou!")