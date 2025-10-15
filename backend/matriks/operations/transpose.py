# backend/Matriks/operations/transpose.py
from ..matrix import Matrix

def transpose(matrix):
    """Menghitung transposisi dari sebuah matriks."""
    transposed_data = [[0 for _ in range(matrix.rows)] for _ in range(matrix.cols)]
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            transposed_data[j][i] = matrix.get_value(i, j)
    return Matrix(transposed_data)