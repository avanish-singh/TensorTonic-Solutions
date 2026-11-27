import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    X = np.array(np.sort(x))
    q_value = np.array(q)
    position = (X.size -1) * (q_value/100)
    l = np.array(np.floor(position), dtype = int)
    u = np.array(np.ceil(position), dtype = int)
    w = position - l
    z = (1-w) * X[l] + w*X[u]
    return z
    
    

    