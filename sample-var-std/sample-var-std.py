import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    #sample variance
    X = np.array(x, dtype = float)
    centred = X - np.mean(X)
    sample_var = np.sum(centred **2)/(X.size - 1)
    std = np.sqrt(sample_var)
    return {
        "variance" : sample_var,
        "standard_deviation" : std
    }
    