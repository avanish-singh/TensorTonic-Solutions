import numpy as np

def svd(A: list) -> dict:
    """
    Returns a dictionary containing float64 arrays U, s, and Vt.
    """
    A_value = np.array(A, dtype = np.float64)
    U, s, Vt = np.linalg.svd(A_value, full_matrices = False)
    for i in range(s.size):
        x = int(np.argmax(np.abs(U[:,i])))
        if U[x,i] < 0:
            U[:,i] *= -1
            Vt[i,:] *= -1
        
        return {
            "U": U.astype(np.float64),
            "s": s.astype(np.float64),
            "Vt": Vt.astype(np.float64)
        }