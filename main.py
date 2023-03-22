initial_shapes = [
    [[0, 0, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 1, 1]],

    [[0, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 1, 1, 1]],

    [[0, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 1],
     [0, 1, 0, 0]],

    [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 1, 1],
     [0, 0, 1, 1]],

    [[0, 0, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 1, 1],
     [0, 0, 1, 0]],

    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 1, 0, 1],
     [0, 1, 1, 1]],

    [[0, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 1],
     [0, 0, 1, 1]],

    [[0, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 1, 1]],

    [[0, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 1],
     [0, 0, 0, 1]],

    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [1, 1, 1, 1]]]


def rotation_90(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][len(matrix) - i - 1] = matrix[i][j]

    return new_matrix