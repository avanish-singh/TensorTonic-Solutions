import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A_value = np.array(A, dtype = float)
    m,n = A_value.shape
    augmented_matrix = np.concatenate((A_value.copy(), np.eye(n, dtype = float)), axis = 1)
    for c in range(n):
        #1 find pivot row
        pivot = c + np.argmax(np.abs(augmented_matrix[c:, c]))
        #2 check pivot is zero
        if abs(augmented_matrix[pivot, c]) < 1e-12:
            return None

        #3 swap row
        augmented_matrix[[c, pivot]] =   augmented_matrix[[pivot, c]] # row swapping

        #4 normalize pivot row
        augmented_matrix[c] = augmented_matrix[c] / augmented_matrix[c,c]

        #5 eliminate other rows
        for r in range(n):
            if r != c:
                augmented_matrix[r] -= augmented_matrix[r,c] * augmented_matrix[c]
                
    return augmented_matrix[:, n:]
        
    