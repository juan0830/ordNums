m1 = [[1,2],[3,4],[5,6,10]]
m2 = [[1,5],[10,1]] 

def encontrar_interseccion(m1,m2):
    i = 0
    temp = []
    interseccion = []
    while i < len(m1):
        j = 0
        while j < len(m1[i]):
            temp.append(m1[i])
            j = j + 1
        i = i + 1
    i = 0
    while i < len(m2):
        j = 0
        while j < len(m2[i]):
            k = 0
            while k < len(temp):
                y = 0
                while y < len(temp[k]):
                    if m2[i][j] == temp[k][y] and m2[i][j] not in interseccion: 
                        interseccion.append(m2[i][j])
                    y = y + 1
                k = k + 1
            j = j + 1
        i = i + 1
    print(interseccion)
encontrar_interseccion(m1,m2)
