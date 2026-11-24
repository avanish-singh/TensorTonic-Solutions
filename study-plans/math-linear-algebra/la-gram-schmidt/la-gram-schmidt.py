import numpy as np

def gram_schmidt(vectors: list) -> np.ndarray:
    """
    Returns a float64 array whose rows form the ordered orthonormal basis.
    """
    
    V = np.array(vectors, dtype=np.float64)
    n = V.shape[0]
    Q = np.zeros(V.shape, dtype=np.float64)
    for k in range(n):
        u = V[k].copy()
        for j in range(k):
            u -= np.dot(Q[j], V[k]) * Q[j]
        Q[k] = u / np.linalg.norm(u)
    return Q
    