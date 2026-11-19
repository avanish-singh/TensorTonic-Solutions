import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    A = np.array(a,dtype=float)
    B = np.array(b, dtype=float)
    Z = np.dot(A,B)
    A_norm = np.sqrt(np.sum(A**2))
    B_norm = np.sqrt(np.sum(B**2))
    if A_norm == 0 or B_norm == 0:
        output = 0
        return float(output)
    cosine_similarity = Z / (A_norm * B_norm)
    return float(cosine_similarity)