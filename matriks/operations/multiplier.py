# matriks/operations/multiplier.py
from ..matrix import Matrix
from ..sparsematrix import SparseMatrix

def _multiply_sparse(matrix1, matrix2):
    """Fungsi perkalian yang sangat efisien khusus untuk SparseMatrix."""
    result_data = {} # Simpan hasil dalam dictionary juga
    # Iterasi hanya pada elemen matrix1 yang tidak nol
    for (r1, c1), v1 in matrix1._sparse_data.items():
        # Iterasi hanya pada elemen matrix2 yang tidak nol
        for (r2, c2), v2 in matrix2._sparse_data.items():
            if c1 == r2: # Kondisi perkalian matriks
                if (r1, c2) not in result_data:
                    result_data[(r1, c2)] = 0
                result_data[(r1, c2)] += v1 * v2

    # Ubah hasil dictionary kembali ke format list of lists
    final_result_data = [[0 for _ in range(matrix2.cols)] for _ in range(matrix1.rows)]
    for (r, c), v in result_data.items():
        final_result_data[r][c] = v
        
    return Matrix(final_result_data)

def _multiply_dense(matrix1, matrix2):
    """Fungsi perkalian standar untuk Matrix biasa."""
    result_data = [[0 for _ in range(matrix2.cols)] for _ in range(matrix1.rows)]
    for i in range(matrix1.rows):
        for j in range(matrix2.cols):
            for k in range(matrix1.cols):
                val1 = matrix1.get_value(i, k)
                val2 = matrix2.get_value(k, j)
                result_data[i][j] += val1 * val2
    return Matrix(result_data)

def multiply_matrices(matrix1, matrix2):
    """Melakukan operasi perkalian pada dua objek matriks."""
    if matrix1.cols != matrix2.rows:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua untuk perkalian.")
    
    # INILAH LOGIKA UTAMANYA:
    # Cek apakah kedua matriks adalah instance dari SparseMatrix
    if isinstance(matrix1, SparseMatrix) and isinstance(matrix2, SparseMatrix):
        return _multiply_sparse(matrix1, matrix2)
    else:
        # Jika salah satu atau keduanya bukan sparse, gunakan metode lama yang aman
        return _multiply_dense(matrix1, matrix2)