""" In this minesweeper the indices of the matrix will be given and you have to replace it with x
and and increase the value of the other element by one if the x is near to the element
"""


def north():
    matrix[i - 1][j] += 1  # increase the top number by 1


def south():
    matrix[i + 1][j] += 1  # increase the bottom number by 1


def east():
    matrix[i][j + 1] += 1  # increase the right number by 1


def west():
    matrix[i][j - 1] += 1  # increase the left number by 1


def northeast():
    matrix[i - 1][j + 1] += 1  # increase the top-right number by 1


def northwest():
    matrix[i - 1][j - 1] += 1  # increase the top-left number by 1


def southwest():
    matrix[i + 1][j - 1] += 1  # increase the bottom-left number by 1


def southeast():
    matrix[i + 1][j + 1] += 1  # increase the bottom-right number by 1


def matrixinput(n):  # get the input of the matrix and return as 2d array
    matri1 = []
    for i in range(n):
        b = []
        for j in range(n):
            p = int(0)
            b.append(p)
        matri1.append(b)
    return matri1


def matrixconversion(matrix):  # replace "x" with respective to the index
    try:
        for i in range(0, (len(a) - 1), 2):
            for j in range(n):
                k = a[i]
                s = a[i + 1]
                matrix[k][s] = "X"
    except IndexError:
        return matrix


n = int(input())
a = []
while True:
    p = str(input())
    if p == 'q':
        break
    else:
        a.append(int(p))
matrix = matrixinput(n)
matrixconversion(matrix)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "X":
            if i == 0 and j == 0:  # the following code is to increase the value 1 according to the indices
                #  i assume this as the 5x5 matrix and wrote the comment
                try:
                    east()
                except TypeError:
                    pass
                try:
                    south()
                except TypeError:
                    pass
                try:
                    southeast()

                except TypeError:
                    pass
            if i == (n - 1) and j == 0:  # 4,0
                try:
                    east()
                except TypeError:
                    pass
                try:
                    north()
                except TypeError:
                    pass
                try:
                    northeast()
                except TypeError:
                    pass
            if i == (n - 1) and j == (n - 1):  # 4,4
                try:
                    west()
                except TypeError:
                    pass
                try:
                    north()
                except TypeError:
                    pass
                try:
                    northwest()

                except TypeError:
                    pass
            if i == 0 and j == (n - 1):  # 0,4
                try:
                    west()
                except TypeError:
                    pass
                try:
                    southwest()
                except TypeError:
                    pass
                try:
                    south()
                except TypeError:
                    pass
            if i == 0 and 1 <= j < (n - 1):  # 0 , (1 or 2 or 3 )
                try:
                    west()
                except TypeError:
                    pass
                try:
                    southwest()
                except TypeError:
                    pass
                try:
                    south()
                except TypeError:
                    pass
                try:
                    southeast()
                except TypeError:
                    pass
                try:
                    east()
                except TypeError:
                    pass
            if j == 0 and 1 <= i < (n - 1):  # (1 or 2 or 3 ) , 0
                try:
                    north()
                except TypeError:
                    pass
                try:
                    northeast()
                except TypeError:
                    pass
                try:
                    east()
                except TypeError:
                    pass
                try:
                    southeast()
                except TypeError:
                    pass
                try:
                    south()
                except TypeError:
                    pass
            if i == (n - 1) and 1 <= j < (n - 1):  # 4,(1 or 2 or 3)
                try:
                    west()
                except TypeError:
                    pass
                try:
                    northwest()
                except TypeError:
                    pass
                try:
                    north()
                except TypeError:
                    pass
                try:
                    northeast()
                except TypeError:
                    pass
                try:
                    east()
                except TypeError:
                    pass
            if j == (n - 1) and 1 <= i < (n - 1): # 1 or 2 or 3 or , 4
                try:
                    north()
                except TypeError:
                    pass
                try:
                    northwest()
                except TypeError:
                    pass
                try:
                    west()
                except TypeError:
                    pass
                try:
                    southwest()
                except TypeError:
                    pass
                try:
                    south()
                except TypeError:
                    pass
            if 1 <= i < (n - 1) and 1 <= j < (n - 1): # 1 or 2 or 3 , 1 or 2 or 3
                try:
                    north()
                except TypeError:
                    pass
                try:
                    northeast()
                except TypeError:
                    pass
                try:
                    east()
                except TypeError:
                    pass
                try:
                    southeast()
                except TypeError:
                    pass
                try:
                    south()
                except TypeError:
                    pass
                try:
                    southwest()
                except TypeError:
                    pass
                try:
                    west()
                except TypeError:
                    pass
                try:
                    northwest()
                except TypeError:
                    pass
for i in range(n):
    print(matrix[i])  # print the resultant matrix
