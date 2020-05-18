from MatrixOperation import MatrixOperation


class SimplexMethod:
    """
    Class to solve games with zero-sum and two players without saddle point
    using mixed strategy using Simplex Method.
    """
    def __init__(self, matrix):
        self.matrix = matrix
        self.solution = list()
        self.tracker = list()

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

    def simplex_method(self, cof_1, cof_2):
        """
        Implementation of Simplex method.
        :return: None
        """
        self.solution = [1 for i in range(len(self.matrix))]
        basic = [cof_1 for i in range(len(self.matrix))]
        nbasic = [cof_2 for i in range(len(self.matrix[0]))]
        r = list()
        counter = 0
        s = 0
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                s += basic[j] * self.matrix[j][i]
            r.append(s - nbasic[i])
            s = 0
        while True:
            for i in range(len(r)):
                if round(r[i], 2) >= 0:
                    counter += 1
            if counter == len(nbasic):
                break
            counter = 0
            m = abs(r[0])
            pointer = 0
            for i in range(len(r)):
                if abs(m) < abs(r[i]) and r[i] < 0:
                    m = r[i]
                    pointer = i
            index_c = pointer
            s_solution = [0 for i in range(len(self.solution))]
            for i in range(len(self.matrix)):
                if self.matrix[i][index_c] > 0:
                    s_solution[i] = self.solution[i] / self.matrix[i][index_c]
                else:
                    s_solution[i] = 1000
            index_r = s_solution.index(min(s_solution))
            basic[index_r], nbasic[index_c] = nbasic[index_c], basic[index_r]
            self.tracker.append([index_r, index_c])
            pivot_element = self.matrix[index_r][index_c]
            self.matrix[index_r][index_c] = 1 / pivot_element
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i != index_r and j != index_c:
                        self.matrix[i][j] = ((pivot_element * self.matrix[i][j]) - (self.matrix[index_r][j] *
                                             self.matrix[i][index_c])) / pivot_element
            for i in range(len(self.solution)):
                if i == index_r:
                    continue
                else:
                    self.solution[i] = ((pivot_element * self.solution[i]) - (self.solution[index_r] *
                                     self.matrix[i][index_c])) / pivot_element
            for i in range(len(r)):
                if i == index_c:
                    continue
                else:
                    r[i] = (pivot_element * r[i] - (self.matrix[index_r][i] * r[index_c])) / pivot_element
            for i in range(len(self.matrix[0])):
                if i == index_c:
                    continue
                else:
                    self.matrix[index_r][i] = self.matrix[index_r][i] / pivot_element
            r[index_c] = r[index_c] / - pivot_element
            self.solution[index_r] = self.solution[index_r] / pivot_element
            for j in range(len(self.matrix)):
                if j == index_r:
                    continue
                self.matrix[j][index_c] = self.matrix[j][index_c] / - pivot_element

    def right_order(self):
        """
        Helping function to make a right order of solutions.
        :return: None
        """
        new_solution = [0 for i in range(len(self.solution))]
        for i in range(len(self.solution)):
            index_1 = self.tracker[i][0]
            index_2 = self.tracker[i][1]
            new_solution[index_2] = self.solution[index_1]
        self.solution = new_solution

    def game_solution(self):
        """
        Solving a game using simplex method.
        :return: list of floats
        """
        self.transform()
        tr = MatrixOperation(self.matrix)
        tr = tr.transpose()
        for i in range(len(tr)):
            for j in range(len(tr[i])):
                tr[i].append(0)
            tr[i][len(tr) + i] = -1
        row_player = SimplexMethod(tr)
        row_player.simplex_method(-1, 0)
        self.simplex_method(0, 1)
        self.right_order()
        row_player.right_order()
        value = 1 / sum(self.solution)
        return list(map(lambda x: x * value, self.solution)), list(map(lambda x: x * value, row_player.solution)), value

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
        return 'Optimal pure strategy for 1st player: ' + first_player + '\n' + 'For the 2nd player: ' + second_player + \
               "\n" + 'The value of a game ' + str(round(ans[2], 2))


if __name__ == "__main__":
    a = SimplexMethod([[0,1,-1, 2],
                       [-1,0,3,2],
                       [0,1,2,-1],
                       [2,0,0,0]])
    print(a)
