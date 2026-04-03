"""
Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's in place.

Example:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Time Complexity: O(m*n)
Space Complexity: O(1)
"""

def setZeroes(matrix):
    """
    Set entire row and column to zero if element is 0.
    Uses first row and column as markers (O(1) space solution).
    """
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Track if first row and first column need to be zeroed
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row has any zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    # Check if first column has any zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # Use first row and column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set rows to zero based on first column marker
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0
    
    # Set columns to zero based on first row marker
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0
    
    # Handle first row
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # Handle first column
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


def setZeroes_simple(matrix):
    """
    Simple O(m+n) space solution using sets to track rows and columns to zero.
    """
    if not matrix:
        return
    
    rows_to_zero = set()
    cols_to_zero = set()
    
    # Find all positions with 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    
    # Set rows to zero
    for row in rows_to_zero:
        for j in range(len(matrix[0])):
            matrix[row][j] = 0
    
    # Set columns to zero
    for col in cols_to_zero:
        for i in range(len(matrix)):
            matrix[i][col] = 0


# Test cases
if __name__ == "__main__":
    # Test case 1
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Test 1 - Input:", matrix1)
    setZeroes(matrix1)
    print("Output:", matrix1)
    print()
    
    # Test case 2
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print("Test 2 - Input:", [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    setZeroes(matrix2)
    print("Output:", matrix2)
    print()
    
    # Test case 3
    matrix3 = [[1, 1], [1, 1]]
    print("Test 3 - Input:", matrix3)
    setZeroes(matrix3)
    print("Output:", matrix3)
