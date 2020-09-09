def add():
    l1 = input('Enter size of first matrix:').split()
    l1[0] = int(l1[0])
    l1[1] = int(l1[1])
    mat = []
    print('Enter first matrix:')
    for i in range(l1[0]):
        row = input().split()
        for j in range(l1[1]):
            row[j] = float(row[j])
        mat.append(row)
    l2 = input('Enter size of second matrix:').split()
    l2[0] = int(l2[0])
    l2[1] = int(l2[1])
    print('Enter second matrix:')
    mat2 = []
    for i in range(l2[0]):
        row = input().split()
        for j in range(l2[1]):
            row[j] = float(row[j])
        mat2.append(row)
    if l1[0] != l2[0] or l1[1] != l2[1]:
        print('The operation cannot be performed.')
    else:
        matr = []
        strin = []
        for a in range(l1[0]):
            for b in range(l1[1]):
                s = mat[a][b] + mat2[a][b]
                strin.append(s)
            matr.append(strin)
            strin = []
        print('The result is:')
        for row in matr:
            print(' '.join(str(col) for col in row))


def mult_by_c():
    l1 = input('Enter size of matrix:').split()
    l1[0] = int(l1[0])
    l1[1] = int(l1[1])
    mat = []
    print('Enter matrix:')
    for i in range(l1[0]):
        row = input().split()
        for j in range(l1[1]):
            row[j] = float(row[j])
        mat.append(row)
    s = int(input('Enter constant:'))
    for i in range(l1[0]):
        for j in range(l1[1]):
            mat[i - 1][j - 1] = s * mat[i - 1][j - 1]
    print('The result is:')
    for row in mat:
        print(' '.join(str(col) for col in row))


def mult():
    l1 = input('Enter size of first matrix:').split()
    l1[0] = int(l1[0])
    l1[1] = int(l1[1])
    mat = []
    print('Enter first matrix:')
    for i in range(l1[0]):
        row = input().split()
        for j in range(l1[1]):
            row[j] = float(row[j])
        mat.append(row)
    l2 = input('Enter size of second matrix:').split()
    l2[0] = int(l2[0])
    l2[1] = int(l2[1])
    mat2 = []
    matr = []
    col = []
    s = 0
    print('Enter second matrix:')
    for i in range(l2[0]):
        row = input().split()
        for j in range(l2[1]):
            row[j] = float(row[j])
        mat2.append(row)
    if l1[1] != l2[0]:
        print('The operation cannot be performed.')
    else:
        for a in range(l1[0]):
            for b in range(l2[1]):
                for k in range(l2[0]):
                    s += mat[a][k] * mat2[k][b]
                col.append(s)
                s = 0
            matr.append(col)
            col = []
        print('The result is:')
        for row in matr:
            print(' '.join(str(col) for col in row))


def trans(ch):
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    if ch == '1':
        l1 = input('Enter size of matrix:').split()
        l1[0] = int(l1[0])
        l1[1] = int(l1[1])
        mat = []
        print('Enter matrix:')
        for i in range(l1[0]):
            row = input().split()
            for j in range(l1[1]):
                row[j] = float(row[j])
            mat.append(row)
        matr = []
        col = []
        s = 0
        for b in range(l1[1]):
            for a in range(l1[0]):
                s = mat[a][b]
                col.append(s)
            matr.append(col)
            col = []
        print('The result is:')
        for row in matr:
            print(' '.join(str(col) for col in row))
    if ch == '2':
        l1 = input('Enter size of matrix:').split()
        l1[0] = int(l1[0])
        l1[1] = int(l1[1])
        mat = []
        print('Enter matrix:')
        for i in range(l1[0]):
            row = input().split()
            for j in range(l1[1]):
                row[j] = float(row[j])
            mat.append(row)
        matr = []
        col = []
        s = 0
        for b in range(l1[0]):
            for a in range(l1[1]):
                s = mat[l1[0] - 1 - a][l1[1] - 1 - b]
                col.append(s)
            matr.append(col)
            col = []
        print('The result is:')
        for row in matr:
            print(' '.join(str(col) for col in row))
    if ch == '3':
        l1 = input('Enter size of matrix:').split()
        l1[0] = int(l1[0])
        l1[1] = int(l1[1])
        mat = []
        print('Enter matrix:')
        for i in range(l1[0]):
            row = input().split()
            for j in range(l1[1]):
                row[j] = float(row[j])
            mat.append(row)
        matr = []
        col = []
        s = 0
        for a in range(l1[0]):
            for b in range(l1[1]):
                s = mat[a][l1[1] - 1 - b]
                col.append(s)
            matr.append(col)
            col = []
        print('The result is:')
        for row in matr:
            print(' '.join(str(col) for col in row))
    if ch == '4':
        l1 = input('Enter size of matrix:').split()
        l1[0] = int(l1[0])
        l1[1] = int(l1[1])
        mat = []
        print('Enter matrix:')
        for i in range(l1[0]):
            row = input().split()
            for j in range(l1[1]):
                row[j] = float(row[j])
            mat.append(row)
        matr = []
        col = []
        for a in range(l1[0]):
            for b in range(l1[1]):
                s = mat[l1[0] - 1 - a][b]
                col.append(s)
            matr.append(col)
            col = []
        print('The result is:')
        for row in matr:
            print(' '.join(str(col) for col in row))


def matrix():
    l1 = input('Enter size of matrix:').split()
    l1[0] = int(l1[0])
    l1[1] = int(l1[1])
    mat = []
    print('Enter matrix:')
    for i in range(l1[0]):
        row = input().split()
        for j in range(l1[1]):
            row[j] = float(row[j])
        mat.append(row)
    return mat, l1


def det(mat, l1):
    if l1[0] != l1[1]:
        print('The operation cannot be performed.')
    else:
        c = 0
        if l1[0] == 1:
            c += mat[0][0]
            return c
        else:
            mat2 = []
            col = []
            for a in range(l1[1]):
                for b in range(1, l1[0]):
                    for d in range(l1[0] - 1):
                        if d < a:
                            col.append(mat[b][d])
                        if d >= a:
                            col.append(mat[b][d + 1])
                    mat2.append(col)
                    col = []
                l2 = [l1[0] - 1, l1[1] - 1]
                if a % 2 == 1:
                    c += - mat[0][a] * det(mat2, l2)
                else:
                    c += mat[0][a] * det(mat2, l2)
                mat2 = []
            return c


def inverse(mat, l, deter):
    minor = []
    mat2 = []
    col = []
    sol = []
    for g in range(l[1]):
        for a in range(l[1]):
            for b in range(l[0] - 1):
                for d in range(l[0] - 1):
                    if d < a and b < g:
                        col.append(mat[b][d])
                    elif d >= a and b < g:
                        col.append(mat[b][d + 1])
                    elif d < a and b >= g:
                        col.append(mat[b + 1][d])
                    else:
                        col.append(mat[b + 1][d + 1])
                mat2.append(col)
                col = []
            l2 = [l[0] - 1, l[1] - 1]
            sol.append(det(mat2, l2))
            mat2 = []
        minor.append(sol)
        sol = []
    for a in range(l[0]):
        for b in range(l[0]):
            if (a + b) % 2 == 1:
                minor[a][b] = -minor[a][b]
    matr = []
    col = []
    for b in range(l[0]):
        for a in range(l[1]):
            s = minor[a][b]
            col.append(s)
        matr.append(col)
        col = []
    s = 1 / deter
    for i in range(l[0]):
        for j in range(l[1]):
            matr[i - 1][j - 1] = s * matr[i - 1][j - 1]
    print('The result is:')
    for row in matr:
        print(' '.join(str(col) for col in row))


while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    ch = input()
    if ch == '1':
        add()
    elif ch == '2':
        mult_by_c()
    elif ch == '3':
        mult()
    elif ch == '4':
        trans(input())
    elif ch == '5':
        mat, l1 = matrix()
        k = det(mat, l1)
        print('The result is:\n', k)
    elif ch == '6':
        mat, l1 = matrix()
        deter = det(mat, l1)
        if det == 0:
            print("This matrix doesn't have an inverse")
        else:
            inverse(mat, l1, deter)
    else:
        break
