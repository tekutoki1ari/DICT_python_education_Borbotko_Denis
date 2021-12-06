

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


def main():
    choose = int(input('''select funct:
                        1 - matrix addition
                        2 - matrix constant multiplication
                        3 - matrix multiplication
                        0 - exit
                        '''))
    if choose == 1:
        matrix_addition()
    elif choose == 2:
        matrix_constant_multiplication()
    elif choose == 3:
        matrix_multiplication()
    elif choose == 0:
        print('bye')
    else:
        print('try again')
        main()


main()
