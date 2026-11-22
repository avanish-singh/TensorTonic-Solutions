import numpy as np

def matrix_determinant(A: list) -> float:
    """
    Returns the determinant as a Python float.
    """
    A_value = np.array(A, dtype=float)
    determinant = np.linalg.det(A_value)
    return float(determinant)
    
    
    