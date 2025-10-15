# backend/regression/linear_regression.py
import numpy as np
from matriks.matrix import Matrix
from matriks.operations.transpose import transpose
from matriks.operations.inverse import inverse
from matriks.operations.multiplier import multiply_matrices

def perform_linear_regression(dataframe):
    """
    Menerima DataFrame, melakukan regresi, dan mengembalikan hasilnya.
    """
    try:
        print("Starting linear regression calculation...")
        
        # Ambil data dari kolom pertama dan kedua
        X_data = dataframe.iloc[:, 0].values
        y_data = dataframe.iloc[:, 1].values
        
        print(f"X_data shape: {X_data.shape}")
        print(f"y_data shape: {y_data.shape}")
        print(f"X_data sample: {X_data[:5]}")
        print(f"y_data sample: {y_data[:5]}")
        
        # PERBAIKAN: Pastikan data numerik dan handle missing values
        X_data = np.array(X_data, dtype=float)
        y_data = np.array(y_data, dtype=float)
        
        # Check for NaN atau infinite values
        if np.any(np.isnan(X_data)) or np.any(np.isnan(y_data)):
            raise ValueError("Data contains NaN values. Please check your CSV file.")
        
        if np.any(np.isinf(X_data)) or np.any(np.isinf(y_data)):
            raise ValueError("Data contains infinite values. Please check your CSV file.")
        
        # Buat matriks X dengan intercept (kolom 1s)
        X_b = np.c_[np.ones((len(X_data), 1)), X_data]
        print(f"X_b shape: {X_b.shape}")
        
        # Konversi ke Matrix objects
        X_matrix = Matrix(X_b.tolist())
        y_matrix = Matrix(y_data.reshape(-1, 1).tolist())
        
        print("Matrices created successfully")
        
        # Rumus Inti: β = (XᵀX)⁻¹Xᵀy
        print("Calculating transpose...")
        X_transpose = transpose(X_matrix)
        
        print("Calculating XᵀX...")
        XTX = multiply_matrices(X_transpose, X_matrix)
        
        print("Calculating (XᵀX)⁻¹...")
        XTX_inverse = inverse(XTX)
        
        print("Calculating Xᵀy...")
        XTy = multiply_matrices(X_transpose, y_matrix)
        
        print("Calculating β...")
        beta_matrix = multiply_matrices(XTX_inverse, XTy)
        
        # Extract coefficients
        intercept = beta_matrix.get_value(0, 0)
        slope = beta_matrix.get_value(1, 0)
        
        print(f"Intercept: {intercept}")
        print(f"Slope: {slope}")
        
        # Hitung titik untuk regression line
        x_min, x_max = float(np.min(X_data)), float(np.max(X_data))
        y_pred_min = slope * x_min + intercept
        y_pred_max = slope * x_max + intercept
        
        regression_line = [
            {'x': x_min, 'y': y_pred_min}, 
            {'x': x_max, 'y': y_pred_max}
        ]
        
        # PERBAIKAN: Konversi numpy types ke Python native types untuk JSON serialization
        result = {
            "original_data": dataframe.values.tolist(),
            "regression_line": regression_line,
            "equation": f"y = {slope:.4f}x + {intercept:.4f}"
        }
        
        print("Linear regression completed successfully")
        return result
        
    except Exception as e:
        print(f"Error in perform_linear_regression: {str(e)}")
        import traceback
        traceback.print_exc()
        raise