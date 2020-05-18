from MatrixOperation import MatrixOperation


class SaddlePoint:
    """
    Class to work with Two-Player Zero-Sum Games: to determine if there is
    a saddle point and calculate it. Moreover, class can determine and delete
    from matrix dominated strategy.
    """
    def __init__(self, matrix):
        """
        Initialisation of matrix.
        :param: matrix: 2D list of number
        """
        self.matrix = matrix
        self.flag = False

    def find_max_min_row(self):
        """
        Find the maximum value among minimum values of each row.
        :return: number
        """
        arr = list()
        for i in range(len(self.matrix)):
            arr.append(min(self.matrix[i]))
        return max(arr)

    def find_min_max_column(self):
        """
        Find the minimum value among maximum values of each column.
        :return: number
        """
        f_arr = list()
        arr = list()
        for j in range(len(self.matrix[0])):
            for i in range(len(self.matrix)):
                arr.append(self.matrix[i][j])
            f_arr.append(max(arr))
            arr = list()
        return min(f_arr)

    def optimal_choice(self, point):
        """
        Return the list of strategies which are optimal for each player.
        :param point: number.
        :return: tuple of two lists
        """
        row = list()
        column = list()
        arr = list()
        for i in range(len(self.matrix)):
            if point in self.matrix[i]:
                row.append(i)
        for j in range(len(self.matrix[0])):
            for i in range(len(self.matrix)):
                arr.append(self.matrix[i][j])
            if point in arr:
                column.append(j)
            arr = list()
        return row, column

    @staticmethod
    def row_domination(matrix, column=False):
        """
        Function which help to find dominated strategy, find out such rows in the matrix.
        :param matrix: 2D list
        :return: 2D list
        """
        counter_1, counter_2 = 0, 0
        weak = list()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                for l in range(len(matrix[i])):
                    if matrix[i][l] <= matrix[j][l] and not column:
                        counter_1 += 1
                    if matrix[i][l] >= matrix[j][l] and not column:
                        counter_2 += 1
                    if matrix[i][l] >= matrix[j][l] and column:
                        counter_1 +=1
                    if matrix[i][l] <= matrix[j][l] and column:
                        counter_2 += 1
                if counter_1 == len(matrix[i]):
                    counter_1, counter_2 = 0, 0
                    if matrix[i] not in weak:
                        weak.append(matrix[i])
                    break
                if counter_2 == len(matrix[i]):
                    counter_1, counter_2 = 0, 0
                    if matrix[j] not in weak:
                        weak.append(matrix[j])
                    break
                counter_1, counter_2 = 0, 0
        i = 0
        while True:
            if matrix[i] in weak:
                weak.remove(matrix[i])
                matrix.remove(matrix[i])
            i += 1
            if not weak:
                break
        return matrix

    @staticmethod
    def convector(lst):
        """
        Function to convert list of numbers into string with these numbers separated by coma.
        :param lst: list of number
        :return: string
        """
        lst = map(lambda x: x + 1, lst)
        lst = map(lambda x: str(x), lst)
        return ','.join(lst)

    def domination(self):
        """
        Function which detect all dominated strategies and delete them from matrix.
        :return: None
        """
        self.row_domination(self.matrix)
        m = MatrixOperation(self.matrix)
        tr = m.transpose()
        tr = self.row_domination(tr, True)
        m.change_matrix(tr)
        self.matrix = m.transpose()

    def saddle_point(self):
        """
        Find saddle point or determine that there is no such point.
        :return: string.
        """
        self.domination()
        m_1 = self.find_max_min_row()
        m_2 = self.find_min_max_column()
        if m_1 == m_2:
            row, column = self.optimal_choice(m_1)
            return "Saddle point: " + str(m_1) + '  Optimal choice for 1st player: ' + \
                              self.convector(row)+ ' Optimal choice for 2nd player: ' + self.convector(column)
        else:
            self.flag = True
            return "There is no saddle point"


if __name__ == "__main__":
    s_1 = SaddlePoint([[4,4,10],
                       [2,3,1],
                       [6,5,7]])
    print(s_1.saddle_point())
