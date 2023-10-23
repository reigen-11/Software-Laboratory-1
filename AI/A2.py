import numpy as np


def valid_moves(current_state, row, col):
    moves = []
    if row > 0:
        moves.append((row - 1, col))

    if row < current_state.shape[0] - 1:
        moves.append((row + 1, col))

    if col > 0:
        moves.append((row, col - 1))

    if col < current_state.shape[1] - 1:
        moves.append((row, col + 1))

    return moves


def f_score(initial_state, goal_state, g_score):
    h_score = int(np.count_nonzero(initial_state != goal_state))
    return h_score + g_score


def eight_puzzle(initial_state, goal_state, g_score=0):
    position = np.where(initial_state == 0)
    row, col = position[0][0], position[1][0]
    possible_moves = valid_moves(initial_state, row, col)

    while not np.array_equal(initial_state, goal_state):
        f_scores_matrices = []
        same_level_matrices = []
        print(f"{initial_state} : F-score : {f_score(initial_state, goal_state, g_score)}")
        for i, tup in enumerate(possible_moves):
            new_state = initial_state.copy()
            new_row, new_col = tup[0], tup[1]
            new_state[new_row, new_col], new_state[row, col] = new_state[row, col], new_state[new_row, new_col]

            f_scores_matrices.append(f_score(new_state, goal_state, g_score + 1))
            same_level_matrices.append(new_state)

        index = f_scores_matrices.index(min(f_scores_matrices))
        initial_state = same_level_matrices[index]
        f_scores_matrices.clear()
        same_level_matrices.clear()
        g_score += 1
        eight_puzzle(initial_state, goal_state, g_score)


init_matrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [0, 7, 8]])

goal_matrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 0]])


eight_puzzle(init_matrix, goal_matrix, 0)
