"""
Rotate Image 90 Degrees Clockwise

Problem: Given an n x n 2D matrix representing an image, rotate it 90 degrees clockwise in-place.

Approach:
1. Transpose the matrix (swap m[i][j] with m[j][i])
2. Reverse each row

Time Complexity: O(n²)
Space Complexity: O(1) - in-place rotation
"""


def rotate(matrix):
    """
    Rotate matrix 90 degrees clockwise in-place.
    
    Args:
        matrix: List[List[int]] - n x n matrix to rotate
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


def rotate_alternative(matrix):
    """
    Alternative approach: Rotate layer by layer (outside to inside)
    Rotate elements in groups of 4 in clockwise direction.
    """
    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Store top
            top = matrix[first][i]
            
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top to right
            matrix[i][last] = top


# Test cases
if __name__ == "__main__":
    # Test 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    for row in matrix1:
        print(row)
    
    rotate(matrix1)
    print("\nAfter rotation:")
    for row in matrix1:
        print(row)
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    # Test 2: 4x4 matrix
    print("\n" + "="*30)
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("Original matrix:")
    for row in matrix2:
        print(row)
    
    rotate(matrix2)
    print("\nAfter rotation:")
    for row in matrix2:
        print(row)
    # Expected: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    
    # Test 3: 2x2 matrix
    print("\n" + "="*30)
    matrix3 = [[1, 2], [3, 4]]
    print("Original matrix:")
    for row in matrix3:
        print(row)
    
    rotate(matrix3)
    print("\nAfter rotation:")
    for row in matrix3:
        print(row)
    # Expected: [[3, 1], [4, 2]]
