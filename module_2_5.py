#Домашняя работа по уроку "Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    matrix=[]
    for row in range(n):
        matrix_row=[]
        for column in range(m):
            matrix_row.append(value)
        matrix.append(matrix_row)
    print(matrix)
get_matrix(2,2, 10)# result1
get_matrix(3,5, 42)# result2
get_matrix(4,2, 13)# result3