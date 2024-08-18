lista = []
for i in range(10):
    num = int(input("insira um numero"))
    lista.append(num)
    if len(lista) >= 10:
        lista.sort()
        print(") menor número é: ",lista[0], "O maior número é: ",lista[-1])