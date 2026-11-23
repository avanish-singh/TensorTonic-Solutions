import numpy as np

def projection_matrix(A: list) -> np.ndarray:
    """
    Returns the float64 projector onto the column space of A.
    """
    A_value = np.array(A, dtype = np.float64)
    P = A_value @ np.linalg.inv(A_value.T @ A_value) @ A_value.T
    return np.float64(P)