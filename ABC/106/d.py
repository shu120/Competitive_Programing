#D - AtCoder Express 2
import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

S = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    _l, r = map(int, input().split())
    S[_l][r] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] += S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]

ans = []

for _ in range(Q):
    p, q = map(int, input().split())

    res = (S[q][q] - S[p - 1][q] - S[q][p - 1] + S[p - 1][p - 1])

    ans.append(str(res))

print("\n".join(ans))
