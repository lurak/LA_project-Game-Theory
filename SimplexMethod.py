# TODO: test code with different games
# Try to understand LU method


class SimplexMethod:
    """
    Class to solve games with zero-sum and two players without saddle point
    using pure strategy.
    There are three methods implemented there to solve such games:
    1). Using Gauss-Jordan Elimination
    2). Using Simplex method by tables
    3). Using Simplex method by LU-factorization
    """
    def __init__(self, matrix):
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

    def simplex_method(self):
        """
        Implementation of Simplex method.
        :return: None
        """
        self.solution = [1 for i in range(len(self.matrix))]
        basic = [0 for i in range(len(self.matrix))]
        nbasic = [1 for i in range(len(self.matrix[0]))]
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
                if r[i] > 0:
                    counter += 1
            if counter == len(nbasic):
                break
            counter = 0
            m = abs(r[0])
            pointer = 0
            for i in range(len(r)):
                if m < abs(r[i]) and r[i] < 0:
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

    def game_solution(self):
        """
        Solving a game using simplex method.
        :return: list of floats
        """
        self.transform()
        self.simplex_method()
        value = 1 / sum(self.solution)
        return list(map(lambda x: x * value, self.solution))


if __name__ == "__main__":
    a = SimplexMethod([[0,-1,1],
                       [1,0,-1],
                       [-1,1,0]])
    print(a.game_solution())
