import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    a = np.array(A)

    n,m = a.shape
    transpose = np.zeros((m,n), dtype = a.dtype)

    for i in range(n):
        for j in range(m):
            transpose[j,i] = a[i,j]

    return (transpose)
    
