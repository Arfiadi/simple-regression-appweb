# backend/regression/linear_regression.py
import numpy as np
# Perhatikan perubahan path impor di bawah ini
from matriks.matrix import Matrix
from matriks.operations.transpose import transpose
from matriks.operations.inverse import inverse
from matriks.operations.multiplier import multiply_matrices

def perform_linear_regression(dataframe):
    """
    Menerima DataFrame, melakukan regresi, dan mengembalikan hasilnya.
    """
    X_data = dataframe.iloc[:, 0].values
    y_data = dataframe.iloc[:, 1].values
    
    X_b = np.c_[np.ones((len(X_data), 1)), X_data]
    
    X_matrix = Matrix(X_b.tolist())
    y_matrix = Matrix(y_data.reshape(-1, 1).tolist())
    
    # Rumus Inti: β = (XᵀX)⁻¹Xᵀy
    X_transpose = transpose(X_matrix)
    XTX = multiply_matrices(X_transpose, X_matrix)
    XTX_inverse = inverse(XTX)
    XTy = multiply_matrices(X_transpose, y_matrix)
    beta_matrix = multiply_matrices(XTX_inverse, XTy)
    
    intercept = beta_matrix.get_value(0, 0)
    slope = beta_matrix.get_value(1, 0)
    
    x_min, x_max = min(X_data), max(X_data)
    y_pred_min = slope * x_min + intercept
    y_pred_max = slope * x_max + intercept
    
    regression_line = [{'x': x_min, 'y': y_pred_min}, {'x': x_max, 'y': y_pred_max}]
    
    return {
        "original_data": dataframe.values.tolist(),
        "regression_line": regression_line,
        "equation": f"y = {slope:.4f}x + {intercept:.4f}"
    }