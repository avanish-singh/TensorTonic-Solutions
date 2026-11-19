import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    X = np.array(x, dtype=float)
    Y = np.array(y, dtype=float)
    result = np.dot(X,Y)
    return float(result)