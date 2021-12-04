
'''Ainda falta criar funções!!!'''
matrix = []
order = int(input("Qual a ordem da matriz? "))

for l in range(order):
    m = []
    for c in range(order):
        c = int(input("Digite valor para linha "+str(l)+" e coluna"+str(c)+" "))
        m.append(c)
    print()
    matrix.append(m)

for l in range(order):
    for c in range(order):
        print(matrix[l][c], end=" ")
    print()

