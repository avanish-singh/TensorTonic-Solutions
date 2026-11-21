import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """
    U = np.array(u, dtype=np.float64)
    V = np.array(v, dtype=np.float64)

    Z = np.outer(U,V)
    return Z