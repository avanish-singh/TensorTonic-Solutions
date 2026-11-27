from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    X = np.array(x, dtype = np.float64)
    X_arranged = np.sort(X)
    avg = np.mean(X_arranged)
    med_value = np.median(X_arranged)
    count = {}
    for i in X_arranged:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    mod_val = 0
    max_count = 0
    for i, c in count.items():
        if c > max_count:
            max_count = c
            mod_val = i

    c = mod_val
    return {
        "mean": avg,
        "median": med_value,
        "mode": c
    }
        