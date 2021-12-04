#
#
# def matrix1():
#     rows = int(input("how many rows do u want to use? "))
#     columns = int(input("how many columns do u want to use? "))
#     matrix = [[0 for x in range(columns)] for y in range(rows)]
#     for y in range(rows):
#         for x in range(columns):
#             matrix[y][x] = int(input("Enter numbers: "))
#     print("\nThe original matrix is...")
#     for y in range(rows):
#         print("\n")
#         for x in range(columns):
#             print(format(matrix[y][x], "5d"), end="")
#     return rows, columns, matrix
#

def matrix_addition():
    matrix_a = []
    matrix_b = []
    matrix_plus = []
    size = input(f'Input matrix size\n>>> ')
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


matrix_addition()
