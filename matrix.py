'''Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц '''

class Matrix:

    def __init__(self, *args):
        self.matrix = list(args)
        
    def __str__(self):
        res = '\n'.join(map(str, self.matrix))
        res = res.replace(",", "").replace("[", "").replace("]", "")        
        return res
   
    def __add__(self, other):
        
        result = Matrix()
        sum_2 = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_2.append (self.matrix[i][j] + other.matrix[i][j])
            result.matrix.append(sum_2) 
            sum_2 = []      
        return result
        
    def __eq__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                 if self.matrix[i][j] == other.matrix[i][j]:
                     return False
        return True         

    def __mul__(self, other):
        p = len(self.matrix[0])
        if p != len(other.matrix):
            ''' Матрицы разной размерности '''
            return False  # raise ValueError
        else:
            result = Matrix()
            sum_2 = [] 
            for i in range(len(self.matrix)):  # по строкам 1 матрицы
                for j in range(len(other.matrix[i])):  
                    sum = 0
                    for k in range (p):
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    sum_2.append(sum)    
                result.matrix.append(sum_2)   
                sum_2 = [] 
        return result


mat_1 = Matrix([2, 3, 4], [3, 5, 8], [1, 0, 2])
mat_3 = Matrix([2, 3, 4], [3, 5, 8], [1, 0, 2])  
print(mat_1)
print()
mat_2 = Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])  
print(mat_2)
print("\n Сумма матриц \n")
print(f"{mat_1 + mat_2}") 
print("\n Сравнение матриц \n")
print(mat_1 == mat_2)
print(mat_1 != mat_3)
print("\n Умножение матриц \n")
print(f"{mat_1 * mat_3}")