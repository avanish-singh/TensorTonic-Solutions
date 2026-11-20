import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    X = np.array(x, dtype = float)
    Y = np.array(y, dtype=float)
    diff = X-Y
    euclid_distance = np.sqrt(np.sum(diff**2))
    return float(euclid_distance)