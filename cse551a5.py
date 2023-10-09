import numpy as np

POS_INF = 1000


def LCS_Len(X, Y):
    m = len(X)
    n = len(Y)

    c = np.zeros((m + 1, n + 1))
    b = np.zeros((m + 1, n + 1))  # default 0 => "diagonal"
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
            else:
                if c[i - 1, j] >= c[i, j - 1]:
                    c[i, j] = c[i - 1, j]
                    b[i, j] = 1  # "up"
                else:
                    c[i, j] = c[i, j - 1]
                    b[i, j] = -1  # "left"

    return c, b


def construct_LCS(b, X, m, n):
    if m == 0 or n == 0:
        return
    if b[m, n] == 0:
        construct_LCS(b, X, m - 1, n - 1)  # diagonal
        print(X[m - 1])
    else:
        if b[m, n] == 1:
            construct_LCS(b, X, m - 1, n)  # up
        elif b[m, n] == -1:
            construct_LCS(b, X, m, n - 1)  # left
        else:
            pass


'''
def ski_match(S, H):
    """
    :param S: heights of skis (sorted)
    :param H: heights of skiers (sorted)
    :return: two memoization matrices C and B, denoting lookup table of values and recursion direction map respectively
    """
    m = len(S)
    n = len(H)

    c = np.ones((n + 1, m + 1)) * POS_INF
    b = np.ones((n + 1, m + 1)) * POS_INF  # default to POS_INF

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c[i, j] = abs(S[j - 1] - H[i - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if c[i, j] <= min(c[i - 1, j], c[i, j - 1]):
                b[i, j] = 0  # diagonal
            else:
                if c[i - 1, j] < c[i, j - 1]:
                    b[i, j] = 1  # up
                elif c[i - 1, j] > c[i, j - 1]:
                    b[i, j] = -1  # left

    return c, b


def construct_opt_match(b, S, H, m, n):
    if m == POS_INF or n == POS_INF:
        return
    if b[m, n] == 0:
        construct_opt_match(b, S, H, m - 1, n - 1)
        print("Skier with height: ", H[m - 1], "matched with ski height: ", S[n - 1])
    else:
        if b[m, n] == 1:
            construct_opt_match(b, S, H, m - 1, n)
            print("Skier with height: ", H[m - 1], "matched with ski height: ", S[n - 1])
        elif b[m, n] == -1:
            construct_opt_match(b, S, H, m, n - 1)
        else:
            pass
'''


def ski_match2(S, H):
    m = len(S)
    n = len(H)

    c = np.zeros((n + 1, m + 1))  # we create the cost matrix i.e., lookup table
    b = np.zeros((n + 1, m + 1))  # we create the recursion direction matrix

    for i in range(n + 1):
        for j in range(m + 1):
            if 1 <= i <= j:  # the "primary" recurrence rule 1 <= i <= j
                if c[i - 1, j - 1] + abs(S[j - 1] - H[i - 1]) <= c[i, j - 1]:  # if the cost of matching s_j to h_i is minimal
                    b[i, j] = 0  # move "diagonally"
                else:
                    b[i, j] = -1  # if that is not the case, we want to move "left"
                c[i, j] = min(c[i, j - 1], c[i - 1, j - 1] + abs(
                    S[j - 1] - H[i - 1]))  # set the cost equal to the minimum of the two in either case
            elif i > j >= 0:  # the "trivial" recurrence rule i > j >= 0
                c[i, j] = POS_INF  # set the cost to infinity
                b[i, j] = 1  # the recursion should move "up"

    # note that c and b are defaulted to 0
    return c, b


def construct_opt_match2(b, S, H, m, n):
    if m == 0 or n == 0:  # if we reach the "boundary" of the matrix, return
        return
    if b[m, n] == 0:  # if we obtained a closest matching, we have a corresponding "diagonal"
        construct_opt_match2(b, S, H, m - 1, n - 1)  # move "diagonally" through the matrix
        print("Skier with height: ", H[m - 1], "matched with ski height: ",
              S[n - 1])  # print the corresponding skier and ski
    else:
        if b[m, n] == 1:  # if we are to go up, a particular ski is unsuitable (or already in use), so move to next skier
            construct_opt_match2(b, S, H, m - 1, n)
        elif b[m, n] == -1:  # if we are to go left, a particular ski does not fit a skier, so move to next ski
            construct_opt_match2(b, S, H, m, n - 1)
        else:
            pass


ski_heights = [60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82]
skier_heights = [61, 63, 64, 67, 68, 69, 71, 76, 78, 78]

# S2 = [1, 3, 4, 5, 6, 8, 14, 16, 19, 100]
# H2 = [3, 4, 6, 7, 14, 17, 18, 19]

c, b = ski_match2(ski_heights, skier_heights)

# print(c)
# print()
# print(b)
# print()

construct_opt_match2(b, ski_heights, skier_heights, len(skier_heights), len(ski_heights))
