# BOJ - 2775 - 01 - B1 - 부녀회장이 될테야
import sys

def resident(k, n):
    apartment = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        apartment[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            apartment[i][j] = apartment[i][j - 1] + apartment[i - 1][j]
    return apartment[k][n]

T = int(sys.stdin.readline().strip())

for i in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(resident(k, n))
