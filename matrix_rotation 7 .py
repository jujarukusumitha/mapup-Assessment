import numpy as np

# Function to rotate matrix and perform the transformation
def rotate_and_transform(matrix):
    n = len(matrix)

    # Step 1: Rotate the matrix by 90 degrees clockwise
    rotated_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

    # Step 2: Replace each element with the sum of all elements in its row and column excluding itself
    transformed_matrix = []
    for i in range(n):
        transformed_row = []
        for j in range(n):
            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]
            col_sum = sum(rotated_matrix[k][j] for k in range(n)) - rotated_matrix[i][j]
            transformed_row.append(row_sum + col_sum)
        transformed_matrix.append(transformed_row)

    return transformed_matrix

# Example input
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Rotate and transform
result = rotate_and_transform(matrix)
print(np.array(result))  # Display matrix in a readable format
