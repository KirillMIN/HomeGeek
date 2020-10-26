
class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        string = ''
        for i in self.list_of_lists:
            for j in i:
                string = string + str(j) + ' '
            string = string + '\n'
        return string

    def __add__(self, other):
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                self.list_of_lists[i][j] = self.list_of_lists[i][j] + other.list_of_lists[i][j]
        return Matrix(self.list_of_lists)


m_1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
m_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(m_1)
print(m_2)
print(m_1 + m_2)
