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
        main()


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
        main()


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
            main()


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
                main()
            elif select == 1:
                print('TRANSPOSED')
                transposed = list(zip(*matrix))
                for i in transposed:
                    print(' '.join(map(str, i)))
                main()
            elif select == 2:
                transposed = []
                for i in range(na):
                    new_list = []
                    for j in reversed(matrix[i]):
                        new_list.append(j)
                    transposed.append(new_list)
                for i in transposed:
                    print(' '.join(map(str, i)))
                main()
            elif select == 3:
                transposed = []
                for i in reversed(matrix):
                    transposed.append(i)
                for i in transposed:
                    print(' '.join(map(str, i)))
                main()
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
    main()


def main():
    select = int(input('''
select funct:
1 - matrix addition
2 - matrix constant multiplication
3 - matrix multiplication
4 - matrix transpose
5 - determinant
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
    elif select == 0:
        print('bye')
    else:
        print('try again')
        main()


main()
