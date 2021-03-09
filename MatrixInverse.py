import sys
cases = 1
matrix = []
for line in sys.stdin:

    if line == "\n":
        cases += 1
        matrix.clear()
    else:
        numbers = line.split()
        matrix.append([int(numbers[0]), int(numbers[1])])
    if len(matrix) == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        adj = [[matrix[1][1], -1 * matrix[0][1]], [matrix[1][0] * -1, matrix[0][0]]]
        inverse = []
        for i in adj:
            for j in i:
                inverse.append(j * det)
        print(f"Case {cases}: \n{inverse[0]} {inverse[1]} \n{inverse[2]} {inverse[3]}")

    if cases > 5:
        break
