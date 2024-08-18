fibonacci = [1]
input = int(input("digite um numero pertencente à sequencia de fibonacci"))
for i in range(input):
    i = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(i)
    print(fibonacci)
    if i == input:
        break