import copy


def matrix_addition():
    matrix_a = []
    matrix_b = []
    matrix_plus = []
    size = input(f'Input matrix size\n: ')
    size = size.replace(' ', '')
    if size.isnumeric():
        size = list(size)
        size_m = int(size[0]) * int(size[1])
        print('Matrix A')
        for i in range(0, int(size_m)):
            number = input(f'Element {i}\n>>> ')
            matrix_a.append(number)
            i += 1
        print('Matrix B')
        for i in range(0, int(size_m)):
            number = input(f'Element {i}\n>>> ')
            matrix_b.append(number)
            i += 1
        for i in range(0, len(matrix_a)):
            matrix_plus.append(int(matrix_a[i]) + int(matrix_b[i]))
            i += 1
        for i in range(0, len(matrix_plus), int(size[1]) + 1):
            matrix_plus.insert(i, '\n')
        print(' '.join(map(str, matrix_plus)))
        menu()


def matrix_constant_multiplication():
    matrix_a = []
    matrix_multiply = []
    size = input(f'Input matrix size\n>>> ')
    size = size.replace(' ', '')
    constant = int(input(f'Input constant\n>>> '))
    if size.isnumeric():
        size = list(size)
        size_m = int(size[0]) * int(size[1])
        print('Matrix A')
        for i in range(0, int(size_m)):
            number = input(f'Element {i}\n>>> ')
            matrix_a.append(number)
            i += 1
        for i in range(0, len(matrix_a)):
            matrix_multiply.append(int(matrix_a[i]) * int(constant))
            i += 1
        for i in range(0, len(matrix_multiply), int(size[1]) + 1):
            matrix_multiply.insert(i, '\n')
        print(' '.join(map(str, matrix_multiply)))
        menu()


def matrix_multiplication():
    matrix_a = []
    matrix_b = []
    size = input(f'Input matrix size\n: ')
    size = size.replace(' ', '')
    m = int(size[0])
    n = int(size[1])
    if size.isnumeric():
        print('Matrix A')
        for i in range(n):
            new_list = []
            for j in range(m):
                number = input(f'Element {j}\n>>> ')
                new_list.append(number)
            matrix_a.append(new_list)
        print('Matrix B')
        for i in range(n):
            new_list = []
            for j in range(m):
                number = input(f'Element {j}\n>>> ')
                new_list.append(number)
            matrix_b.append(new_list)
        r = []
        m = []
        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                sums = 0
                for k in range(len(matrix_b)):
                    sums = sums + (int(matrix_a[i][k]) * int(matrix_a[k][j]))
                r.append(sums)
            m.append(r)
            r = []
        for i in m:
            print(' '.join(map(str, i)))
            menu()


def matrix_transpose():
    matrix = []
    size = input('Input size matrix\n>>> ')
    size = size.replace(' ', '')
    try:
        int(size[0])
        ma = int(size[0])
        na = int(size[1])
        print('Matrix')
        for i in range(0, ma):
            new_list = []
            for j in range(na):
                number = input(f'Element {j}\n>>> ')
                new_list.append(number)
            matrix.append(new_list)
        for i in matrix:
            print(' '.join(map(str, i)))

        print('''
1. Main diagonal
2. Vertical line
3. Horizontal line
0. Back 
''')
        select = input('\n>>> ')
        if select.isnumeric():
            select = int(select)
            if select == 0:
                menu()
            elif select == 1:
                print('TRANSPOSED')
                transposed = list(zip(*matrix))
                for i in transposed:
                    print(' '.join(map(str, i)))
                menu()
            elif select == 2:
                transposed = []
                for i in range(na):
                    new_list = []
                    for j in reversed(matrix[i]):
                        new_list.append(j)
                    transposed.append(new_list)
                for i in transposed:
                    print(' '.join(map(str, i)))
                menu()
            elif select == 3:
                transposed = []
                for i in reversed(matrix):
                    transposed.append(i)
                for i in transposed:
                    print(' '.join(map(str, i)))
                menu()
    except ValueError:
        print('Try Again!')
        matrix_transpose()


def determinant():
    matrix_def = []
    size = input('Input size matrix\n>>> ')
    size = size.replace(' ', '')
    na = int(size[1])
    print('Matrix')
    for i in range(0, na):
        line_def = []
        for j in range(0, na):
            line_def.append(int(input(f'Element {j}\n>>> ')))
        matrix_def.append(line_def)

    def calc(n, matrix):
        if n == 2:
            d = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return d
        else:
            d = int(0)
            temp = copy.deepcopy(matrix)
            line = copy.deepcopy(temp[0])
            temp.pop(0)
            for j in range(0, n):
                temp2 = copy.deepcopy(temp)
                for k in range(0, n - 1):
                    temp2[k].pop(j)
                d += ((-1) ** (0 + j + 2)) * line[j] * (calc(n - 1, temp2))
            return d

    for i in matrix_def:
        print(' '.join(map(str, i)))
    print(f'Your determinant:  {str(calc(na, matrix_def))}')
    menu()


def inverse_matrix():
    matrix = []
    size = input('Input size matrix\n>>> ')
    size = size.replace(' ', '')
    m = int(size[0])
    n = int(size[1])
    print('Matrix')
    for i in range(0, n):
        line = []
        for j in range(0, m):
            line.append(int(input(f'Element {j}\n>>> ')))
        matrix.append(line)

    def gen_id_mat(n):
        l = [[0 for i in range(n)] for j in range(n)]
        for k in range(n):
            l[k][k] = 1
        return l

    def gen_id_mat1(n):
        l = [[0.0 for i in range(n)] for j in range(n)]
        for k in range(n):
            l[k][k] = 1.0
        return l

    def row_swap(m, r1, r2):
        m[r1], m[r2] = m[r2], m[r1]
        return m

    def row_op_1(m, r1, r2, c):
        for i in range(len(m)):
            m[r1][i] = (m[r2][i]) * c
        return m

    def row_op_2(m, r1, r2, c):
        for i in range(len(m)):
            m[r1][i] = m[r1][i] - (c * m[r2][i])
        return m

    def disp(m):
        print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in m]))
        pass

    idm = gen_id_mat(n)
    id_inv = gen_id_mat(n)

    count = 0
    for col in range(n):
        for row in range(n):
            if idm[row][col] == 1 and matrix[row][col] == 0:
                for g in range(n):
                    if matrix[g][col] != 0:
                        matrix = row_swap(matrix, row, g)

            if matrix[row][col] != 0 and idm[row][col] == 1:
                # multiply = 1 / matrix[row][col]
                id_inv = row_op_1(id_inv, row, row, (1 / matrix[row][col]))
                matrix = row_op_1(matrix, row, row, (1 / matrix[row][col]))
                count += 1
                for const in range(n):
                    if const == row:
                        continue
                    # multiply = matrix[const][col]
                    id_inv = row_op_2(id_inv, const, row, matrix[const][col])
                    matrix = row_op_2(matrix, const, row, matrix[const][col])

                    count += 1

    if matrix == gen_id_mat1(n):
        print("Your matrix:")
        print()
        disp(id_inv)
        menu()
    else:
        print("This matrix cant be inverse")
        inverse_matrix()


def menu():
    select = int(input('''
select funct:
1 - matrix addition
2 - matrix constant multiplication
3 - matrix multiplication
4 - matrix transpose
5 - determinant
6 - inverse matrix
0 - exit
'''))
    if select == 1:
        matrix_addition()
    elif select == 2:
        matrix_constant_multiplication()
    elif select == 3:
        matrix_multiplication()
    elif select == 4:
        matrix_transpose()
    elif select == 5:
        determinant()
    elif select == 6:
        inverse_matrix()
    elif select == 0:
        print('bye')
    else:
        print('try again')
        menu()


menu()
