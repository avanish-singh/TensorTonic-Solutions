import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """
    A_matrix = np.array(A, dtype = np.float64)
    B_matrix = np.array(B, dtype = np.float64)
    C = A_matrix @ B_matrix
    return C