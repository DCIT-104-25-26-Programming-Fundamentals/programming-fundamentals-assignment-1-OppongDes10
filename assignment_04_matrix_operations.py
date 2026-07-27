

def read_matrix(prompt):
    """Read a matrix from user input."""
    print(prompt)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").strip().split()))
        if len(row) != cols:
            print("Error: Incorrect number of elements in row.")
            return None
        matrix.append(row)
    return matrix


def print_matrix(matrix, title):
    """Print matrix in a neat, aligned format."""
    if not matrix or not matrix[0]:
        return
    print(f"\n{title}")
    for row in matrix:
        for num in row:
            print(f"{num:4}", end=" ")
        print()


def transpose(matrix):
    """Return the transpose of a matrix using nested loops."""
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b):
    """Add two matrices of the same size using nested loops."""
    if not a or not b or len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    rows = len(a)
    cols = len(a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b):
    """Multiply two matrices using nested loops (A x B)."""
    if not a or not b or len(a[0]) != len(b):
        return None
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result



if  "__main__":
    print("=== MATRIX OPERATIONS PROGRAM ===\n")
    
    print("PART A - Transpose a Matrix")
    mat = read_matrix("Enter matrix to transpose:")
    if mat:
        transposed = transpose(mat)
        print_matrix(mat, "Original Matrix:")
        print_matrix(transposed, "Transposed Matrix:")
    
    
    print("\n" + "="*50)
    print("PART B - Add Two Matrices")
    mat1 = read_matrix("Enter first matrix:")
    mat2 = read_matrix("Enter second matrix:")
    if mat1 and mat2:
        result_add = add_matrices(mat1, mat2)
        if result_add:
            print_matrix(mat1, "Matrix A:")
            print_matrix(mat2, "Matrix B:")
            print_matrix(result_add, "Sum (A + B):")
        else:
            print("Error: Matrices must be the same size.")
    

    print("\n" + "="*50)
    print("PART C - Multiply Two Matrices")
    mat_a = read_matrix("Enter first matrix (A):")
    mat_b = read_matrix("Enter second matrix (B):")
    if mat_a and mat_b:
        result_mul = multiply_matrices(mat_a, mat_b)
        if result_mul:
            print_matrix(mat_a, "Matrix A:")
            print_matrix(mat_b, "Matrix B:")
            print_matrix(result_mul, "Product (A × B):")
        else:
            print("Error: Number of columns in A must equal number of rows in B.")
