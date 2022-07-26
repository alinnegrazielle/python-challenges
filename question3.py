
matrix = []
order = int(input("Qual a ordem da matriz? "))

def preencher(o):
    for l in range(o):
        m = []
        for c in range(o):
            c = int(input("Digite valor para linha "+str(l)+" e coluna "+str(c)+": "))
            m.append(c)
        print()
        matrix.append(m)

def mostrar(o):
    for l in range(o):
        for c in range(o):
            print(matrix[l][c], end=" ")
        print()

preencher(order)
mostrar(order)