from MatrixOperation import MatrixOperation


class GJ:
    """
    Class to solve games with zero-sum and two players without saddle point
    using mixed strategy by GJ elimination.
    """
    def __init__(self, matrix):
        """
        Initialisation of the matrix.
        :param matrix: 2D list of numbers.
        """
        self.matrix = matrix
        self.solution = list()

    def transform(self):
        """
        Make a list of solutions and transform matrix if it has non-positive entries.
        :return: None
        """
        self.solution = [1 for i in range(len(self.matrix))]
        m = self.matrix[0][0]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if m > self.matrix[i][j]:
                    m = self.matrix[i][j]
        for i in range(len(self.matrix)):
            self.matrix[i] = list(map(lambda x: x + abs(m) + 1, self.matrix[i]))

    def gj_method(self):
        """
        Using Gauss-Jordan Elimination to solve matrix game.
        :return: None
        """
        for i in range(len(self.matrix)):
            self.solution[i] = self.solution[i] / self.matrix[i][i]
            self.matrix[i] = list(map(lambda x: x / self.matrix[i][i], self.matrix[i]))
            row = self.matrix[i]
            for j in range(len(self.matrix)):
                element = -self.matrix[j][i]
                row = list(map(lambda x: x * -self.matrix[j][i], row))
                if list(map(lambda x: x / -1, self.matrix[j])) == row:
                    row = self.matrix[i]
                    continue
                self.solution[j] += element * self.solution[i]
                for k in range(len(self.matrix)):
                    self.matrix[j][k] += row[k]
                row = self.matrix[i]

    def pure_strategy(self):
        """
        Find pure solution to matrix game.
        :return: tuple of lists
        """
        tr = MatrixOperation(self.matrix)
        an_pl = GJ(tr.transpose())
        self.transform()
        self.gj_method()
        an_pl.transform()
        an_pl.gj_method()
        value = 1/(sum(self.solution))
        return list(map(lambda x: x*value, self.solution)), list(map(lambda x: x*value, an_pl.solution)), value

    def __str__(self):
        """
        Represent the solution to the game and value.
        :return: String
        """
        ans = self.pure_strategy()
        first_player = str()
        second_player = str()
        for i in range(len(ans[1])):
            first_player += str(round(ans[1][i], 2)) + ' '
            second_player += str(round(ans[0][i], 2)) + ' '
        return 'Optimal pure strategy for 1st player: ' + first_player + '\n' + 'For the 2nd player: ' + second_player +\
               "\n" + 'The value of a game ' + str(round(ans[2], 2))


if __name__ == "__main__":
    a = GJ([[0,1,-1,2],
            [-1,0,3,2],
            [0,1,2,-1],
            [2,0,0,0]
            ])
    print(a)
