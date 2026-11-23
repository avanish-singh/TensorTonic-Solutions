import numpy as np

def vector_projection(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 projection of u onto v.
    """
    U_value = np.array(u, dtype = np.float64)
    V_value = np.array(v, dtype = np.float64)
    projection = (np.dot(U_value, V_value) / np.dot(V_value, V_value)) * V_value
    return np.float64(projection)