def TriverseMatrix(matrix):
    for row_number in range(len(matrix)):
        for column_element in range(row_number, len(matrix[row_number])):
            print(f"The element of row {row_number} and column {column_element} is : {matrix[row_number][column_element]}")



matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

TriverseMatrix(matrix)