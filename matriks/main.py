# matriks/main.py
import time
from .matrix import Matrix
from .sparsematrix import SparseMatrix
from .operations.adder import add_matrices
from .operations.multiplier import multiply_matrices
from .exporters.csv_exporter import export_to_csv
from .exporters.json_exporter import export_to_json

def create_sparse_data(size):
    data = [[0] * size for _ in range(size)]
    data[0][0] = 1
    data[size - 1][size - 1] = 1
    return data

if __name__ == "__main__":
    # --- Menguji Performa SparseMatrix ---
    print("\n--- Menguji Masalah Performa ---")
    sparse_data_1000 = create_sparse_data(1000)
    mat_a = Matrix(sparse_data_1000)
    mat_b = Matrix(sparse_data_1000)

    start_time = time.time()
    product_mat = multiply_matrices(mat_a, mat_b)
    end_time = time.time()
    print(f"Waktu yang dibutuhkan untuk perkalian matriks biasa: {end_time - start_time:.4f} detik")

    print("\n--- Menguji Solusi dengan SparseMatrix ---")
    mat_a_sparse = SparseMatrix(sparse_data_1000)
    mat_b_sparse = SparseMatrix(sparse_data_1000)
    
    start_time = time.time()
    product_mat_sparse = multiply_matrices(mat_a_sparse, mat_b_sparse)
    end_time = time.time()
    print(f"Waktu yang dibutuhkan untuk perkalian matriks sparse: {end_time - start_time:.4f} detik")

    # --- Pembuktian Penjumlahan (OCP) ---
    print("\n--- Pembuktian OCP dengan Penjumlahan ---")
    matriks_padat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriks_jarang = SparseMatrix([[1, 0, 0], [0, 5, 0], [7, 0, 9]])
    
    hasil_penjumlahan = add_matrices(matriks_padat, matriks_jarang)
    print("Hasil Penjumlahan Matriks Biasa dan Sparse:")
    for row in hasil_penjumlahan.data:
        print(row)

    # --- Menguji Exporters ---
    print("\n--- Menguji Matrix Exporters ---")
    matriks_demo = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("Mengekspor matriks ke format CSV...")
    export_to_csv(matriks_demo, "matriks_output.csv")
    
    print("\nMengekspor matriks ke format JSON...")
    export_to_json(matriks_demo, "matriks_output.json")