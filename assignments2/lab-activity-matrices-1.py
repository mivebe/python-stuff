# 1 зад. Дадена е квадратна матрица от реални числа с размерност (n х n),
# където 1n20. Да се състави програма, съдържаща подпрограми за: 
# а) запълване на матрицата с числа от клавиатурата;

# б)намиране на минималния от всички ненулеви елементи под главния диагонал
# включително; ако ненулеви елементи няма, за минимален елемент се приема 0;
	
# Вход:
# 5
# 1 7 3 5 4
# -1 8 0 0 3
# 14 0 0 -6 4
# 4 1 0 -10 -6
# 85 14 -3 0 4
# Изход:
# 	1

# в)извеждане на елементите на матрицата под главния диагонал на екрана.
# Вход:
# 5
# 1 7 3 5 4
# -1 8 0 0 3
# 14 0 0 -6 4
# 4 1 0 -10 -6
# 85 14 -3 0 4
# Изход:
# 	-1
#  14 0
#  4 1 0 
#  85 14 -3 0 


# Да се състави програма matrix1, която като използва описаните подпрограми,
# запълва матрицата с числа от клавиатурата, преобразува я като запълва контура
# на матрицата с намерения от подточка б) елемент и извежда новополучената матрица на екрана.

# а)
def fill_matrix():
    n = int(input())
    if n < 1 or n > 20:
        print("Error: n must be between 1 and 20")
        exit()
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("Error: Each row must have n elements")
            exit()
        matrix.append(row)
    return matrix, n

# б)
def min_below_diagonal(matrix, n):
    min_val = None
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] > 0:
                if min_val is None or matrix[i][j] < min_val:
                    min_val = matrix[i][j]
    if min_val is None:
        return 0
    return min_val

# в)
def print_below_diagonal(matrix, n):
    for i in range(1, n):
        row_elements = []
        for j in range(i):
            row_elements.append(str(int(matrix[i][j]) if matrix[i][j] == int(matrix[i][j]) else matrix[i][j]))
        print(" ".join(row_elements))

def print_matrix(matrix, n):
    for i in range(n):
        row_elements = []
        for j in range(n):
            val = matrix[i][j]
            if val == int(val):
                row_elements.append(str(int(val)))
            else:
                row_elements.append(str(val))
        print(" ".join(row_elements))

def fill_contour(matrix, n, value):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                matrix[i][j] = value
    return matrix

matrix, n = fill_matrix()

print("--- б) Minimum positive element on/below diagonal ---")
min_elem = min_below_diagonal(matrix, n)
if min_elem == int(min_elem):
    print(int(min_elem))
else:
    print(min_elem)

print("\n--- в) Elements below main diagonal ---")
print_below_diagonal(matrix, n)

print("\n--- Final: Matrix with contour filled ---")
matrix = fill_contour(matrix, n, min_elem)
print_matrix(matrix, n)
