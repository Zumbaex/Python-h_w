class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        m = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

        for i in range(len(self.mat)):
            for z in range(len(self.mat[i])):
                m[i][z] = self.mat[i][z] + other.mat[i][z]

        return Matrix(m)

    def __str__(self):
        n = ''
        for i in range(len(self.mat)):
            n = n + '\t'.join(map(str, self.mat[i])) + '\n'
        return n


m = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
print(m)
g = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
print(m + g)
