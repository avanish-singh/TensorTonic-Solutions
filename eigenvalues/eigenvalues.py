import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    A = np.array(matrix, dtype = np.float64)
    eigenValues = np.linalg.eigvals(A)
    Evalues = np.real(np.sort(eigenValues))
    return np.array(Evalues, dtype = np.float64)