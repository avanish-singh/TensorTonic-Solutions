import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    V = np.array(v,dtype=float)
    V1 = np.abs(V)
    L1 = np.sum(V1)
    L2 = np.sqrt(np.sum(V ** 2))
    inf_norm = np.max(V1)
    return np.array([L1, L2, inf_norm], dtype=np.float64)