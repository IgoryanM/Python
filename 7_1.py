class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx

    def __str__(self):
        for el in self.mtx:
            for n in el:
                print(f'{n}', end=' ')
            print()
        return ''

    def __add__(self, mx2):
        new_matrix = []
        result = []
        j = 0
        for el in self.mtx:
            i = 0
            for n in el:
                n = n + mx2.mtx[j][i]
                result.append(n)
                i += 1
            new_matrix.append(result)
            result = []
            j += 1
        return Matrix(new_matrix)


mx_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mx_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mx_3 = mx_1 + mx_2
print(mx_3)
