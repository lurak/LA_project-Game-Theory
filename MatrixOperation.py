class MatrixOperation:
    def __init__(self, matrix):
        self.matrix = matrix

    def change_matrix(self, matrix):
        self.matrix = matrix

    def transpose(self):
        tr = list()
        row = list()
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                row.append(self.matrix[j][i])
            tr.append(row)
            row = list()
        return tr
