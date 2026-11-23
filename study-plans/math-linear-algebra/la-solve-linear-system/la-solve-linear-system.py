import numpy as np

def solve_linear_system(A: list, b: list) -> np.ndarray:
    """
    Returns the float64 solution vector.
    """
    A_value = np.array(A, dtype = np.float64)
    B_value = np.array(b, dtype = np.float64)
    solution = np.linalg.solve(A_value, b)
    return np.float64(solution)
    