class MatrixOperation:
    """
    Help class for some basic matrix operation.
    """
    def __init__(self, matrix):
        """
        Initialization of a matrix.
        :param matrix: 2D list of numbers.
        """
        self.matrix = matrix

    def change_matrix(self, matrix):
        """
        Change a matrix for a class.
        :param matrix: 2D list of numbers.
        :return: None
        """
        self.matrix = matrix

    def transpose(self):
        """
        Return transpose matrix to the given one.
        :return: 2D list of numbers
        """
        tr = list()
        row = list()
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                row.append(self.matrix[j][i])
            tr.append(row)
            row = list()
        return tr
