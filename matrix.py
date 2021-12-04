def showMatrix(matrix):
    for l in matrix:
        print(l)

order = int(input("Qual a ordem da matriz? "))

matrix = []
for l in range(order):
    for c in range(order):
        matrix.append([]*order)

showMatrix(matrix)