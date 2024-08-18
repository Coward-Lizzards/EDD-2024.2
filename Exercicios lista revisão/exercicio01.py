lista = []
for i in range(3):
    num = int(input("Insira um numero"))
    lista.append(num)
    print(lista)  
if len(lista) == 3:
    media = ((lista[0] + lista[1] + lista[2]) / len(lista))
    print(f"A média é: ", media)