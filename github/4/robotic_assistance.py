import numpy as np

def multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def get_determinant(matrix):
    return np.linalg.det(matrix)

def get_inverted_matrix(matrix):
    return np.linalg.inv(matrix)

def get_list_of_matrices(lines, number_of_matrices, size_of_matrix ):
    list_of_matrices = []
    #number_of_lines = number_of_matrices * size_of_matrix

    for mat in range(0, number_of_matrices):
        matrix = [] 
        for line in lines[mat * size_of_matrix + 1 : mat * size_of_matrix + size_of_matrix + 1]:
            matrix.append( list(map(int, line.split())))
        list_of_matrices.append(matrix)
    return list_of_matrices

def find_matrices_with_max_determinant(number_of_matrices,list_of_matrices):
    max_determ = -9999999.0
    indices = None
    for i in range(number_of_matrices):
        for j in range(i + 1, number_of_matrices):
            determ = get_determinant(multiply(list_of_matrices[i], list_of_matrices[j]))
            if determ > max_determ:
                max_determ = determ
                indices = (i, j)
    return indices

def get_result_matrix(list_of_matrices, index_of_matrix_1, index_of_matrix_2):
    determ_matrix1 = get_determinant(list_of_matrices[index_of_matrix_1])
    determ_matrix2 = get_determinant(list_of_matrices[index_of_matrix_2])

    if determ_matrix1 >= determ_matrix2:
        return multiply(list_of_matrices[index_of_matrix_1], list_of_matrices[index_of_matrix_2])
    else:
        return multiply(list_of_matrices[index_of_matrix_2], list_of_matrices[index_of_matrix_1])

def display_matrix(matrix):
    for row in matrix:
        for col in row:
            print(f'{col:.3f}', end =' ')
        print()

    
file = open('input1.txt', 'r')

read_lines = file.read().splitlines()

number_of_matrices, size_of_matrix = map(int, read_lines[0].split())

list_of_matrices = get_list_of_matrices(read_lines, number_of_matrices, size_of_matrix )

indices_of_max = find_matrices_with_max_determinant(number_of_matrices,list_of_matrices)

result_matrix = get_result_matrix(list_of_matrices, indices_of_max[0], indices_of_max[1])

key_matrix = get_inverted_matrix(result_matrix)

display_matrix(key_matrix)
