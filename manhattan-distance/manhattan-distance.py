import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    X = np.array(x, dtype = float)
    Y = np.array(y, dtype = float)
    diff = np.abs(X-Y)
    distance = np.sum(diff)
    return float(distance)