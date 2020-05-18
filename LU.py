from MatrixOperation import MatrixOperation


class LU:
    """
    Class to solve games with zero-sum and two players without saddle point
    using mixed strategy by LU factorization.
    """
    def __init__(self, matrix):
        """
        Initialization of matrix.
        :param matrix: 2D list of numbers
        """
        self.matrix = matrix
        self.U = list()
        self.L = list()
        self.solution = [1 for i in range(len(self.matrix))]

    def lu_factorization(self):
        """
        Function to make LU factorization of matrix, find L and U matrices.
        :return: None
        """
        for i in range(len(self.matrix)):
            tr = MatrixOperation(self.matrix)
            self.U.append(self.matrix[i])
            tr = tr.transpose()
            self.L.append(tr[i])
            if i == len(self.matrix):
                break
            pivot = self.matrix[i][i]
            row = self.matrix[i]
            for j in range(i + 1, len(self.matrix)):
                element = self.matrix[j][i]
                for k in range(i, len(self.matrix)):
                    self.matrix[j][k] = self.matrix[j][k] + (row[k] * (- (element/pivot)))

    def l_transformation(self):
        """
        Helping function of find L.
        :return: None
        """
        for i in range(len(self.L)):
            pivot = self.L[i][i]
            self.L[i] = list(map(lambda x: x / pivot, self.L[i]))
            for j in range(len(self.L[i])):
                if j < i:
                    self.L[i][j] = 0
        tr = MatrixOperation(self.L)
        self.L = tr.transpose()

    def lu_solving(self):
        """
        Find a solution to the game, by solving Ax=b, using l and U.
        :return: None
        """
        self.lu_factorization()
        self.l_transformation()
        for i in range(len(self.L)):
            for j in range(i + 1, len(self.L)):
                self.solution[j] = self.solution[j] + self.solution[i] * (-self.L[j][i])
                self.L[j][i] = 0
        for i in range(len(self.U)-1, -1, -1):
            counter = 1
            pivot = self.U[i][i]
            self.U[i] = list(map(lambda x: x / pivot, self.U[i]))
            self.solution[i] = self.solution[i] / pivot
            for j in range(i - counter + 1):
                self.solution[j] = self.solution[j] + self.solution[i] * (-self.U[j][i])
            counter += 1

    def game_solution(self):
        """
        Solve a game by LU factorization.
        :return: List of lists of numbers.
        """
        tr = MatrixOperation(self.matrix)
        tr = tr.transpose()
        row_p = LU(tr)
        self.lu_solving()
        row_p.lu_solving()
        value = 1/sum(self.solution)
        return list(map(lambda x: x * value, self.solution)), list(map(lambda x: x * value, row_p.solution)), value

    def __str__(self):
        """
        Represent the solution to the game and value.
        :return: String
        """
        ans = self.game_solution()
        first_player = str()
        second_player = str()
        for i in range(len(ans[1])):
            first_player += str(round(ans[1][i], 2)) + ' '
            second_player += str(round(ans[0][i], 2)) + ' '
        return 'Optimal pure strategy for 1st player: ' + first_player + '\n' + 'For the 2nd player: ' + second_player +\
               "\n" + 'The value of a game ' + str(round(ans[2], 2))


if __name__ == "__main__":
    a = LU([[2,1,3],
           [3,2,1],
           [1,3,2]])
    print(a)
