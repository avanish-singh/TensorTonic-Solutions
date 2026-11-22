import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A_value = np.array(A, dtype =float)
    B = []
    m,n = A_value.shape
    for i in range(m):
        for j in range(n):
            if i == j:
                x = A_value[i][j]
                B.append(x)
    trace = np.sum(B)
    return float(trace)
            
            
    