# backend/matriks/operations/inverse.py
from ..matrix import Matrix

def _get_minor(m_data, i, j):
    return [row[:j] + row[j+1:] for row in (m_data[:i] + m_data[i+1:])]

def _get_determinant(m_data):
    if len(m_data) == 2:
        return m_data[0][0] * m_data[1][1] - m_data[0][1] * m_data[1][0]
    determinant = 0
    for c in range(len(m_data)):
        minor = _get_minor(m_data, 0, c)
        determinant += ((-1) ** c) * m_data[0][c] * _get_determinant(minor)
    return determinant

def inverse(matrix):
    """Menghitung invers dari sebuah matriks persegi."""
    if matrix.rows != matrix.cols:
        raise ValueError("Matrix must be square to have an inverse.")

    determinant = _get_determinant(matrix.data)
    if determinant == 0:
        raise ValueError("Determinant is zero, matrix has no inverse.")

    if matrix.rows == 2:
        inv_det = 1 / determinant
        inv_data = [
            [matrix.get_value(1, 1) * inv_det, -matrix.get_value(0, 1) * inv_det],
            [-matrix.get_value(1, 0) * inv_det, matrix.get_value(0, 0) * inv_det]
        ]
        return Matrix(inv_data)

    cofactors = []
    for r in range(matrix.rows):
        cofactor_row = []
        for c in range(matrix.cols):
            minor = _get_minor(matrix.data, r, c)
            cofactor_row.append(((-1) ** (r + c)) * _get_determinant(minor))
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[j][i] for j in range(len(cofactors))] for i in range(len(cofactors[0]))]

    inv_det = 1 / determinant
    for r in range(len(adjugate)):
        for c in range(len(adjugate[0])):
            adjugate[r][c] *= inv_det

    return Matrix(adjugate)