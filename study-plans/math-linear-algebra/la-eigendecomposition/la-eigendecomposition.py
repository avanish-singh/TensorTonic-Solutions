import numpy as np

def eigendecompose(A: list) -> dict:
    """
    Returns sorted float64 eigenvalues and eigenvectors in a dictionary.
    """
    A_value = np.array(A, dtype = np.float64)
    eigenValues, eigenVectors = np.linalg.eig(A_value) # .eig give both eigen value and column-oriented eigenvectors
    index = np.argsort(eigenValues)[::-1]
    eigenValues = eigenValues[index]
    eigenVectors = eigenVectors[:, index]
    eigenVectors /= np.linalg.norm(eigenVectors, axis = 0, keepdims=True)

    return {
        "eigenvalues" : np.array(eigenValues, dtype = np.float64),
        "eigenvectors" : np.array(eigenVectors,dtype = np.float64)
    }
    
    