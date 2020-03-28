def saddle_point(matrix):
    m_1 = find_max_min_row(matrix)
    m_2 = find_min_max_column(matrix)
    if m_1 == m_2:
        row, column = optimal_choice(m_1, matrix)
        return "Saddle point: " + str(m_1) + '  Optimal choice for 1st player: ' + str(row) +\
               'Optimal choice for 2nd player' + str(column)
    else:
        return "There is no saddle point"


def optimal_choice(m, matrix):
    row = list()
    column = list()
    arr = list()
    for i in range(len(matrix)):
        if m in matrix[i]:
            row.append(i)
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            arr.append(matrix[i][j])
        if m in arr:
            column.append(j)
        arr = list()
    return row, column


def find_max_min_row(matrix):
    arr = list()
    for i in range(len(matrix)):
        arr.append(min(matrix[i]))
    return max(arr)


def find_min_max_column(matrix):
    f_arr = list()
    arr = list()
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            arr.append(matrix[i][j])
        f_arr.append(max(arr))
        arr = list()
    return min(f_arr)


if __name__ == "__main__":
    print(saddle_point([[4,5,5,8],
                        [6,7,6,9],
                        [5,7,5,4],
                        [6,6,5,5]]))
