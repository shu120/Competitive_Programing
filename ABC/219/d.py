# D - Strange Lunchbox
N = int(input())
X, Y = map(int, input().split())

INF = float("inf")
A = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append((a, b))

dp = [[[INF] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0

for i in range(N):
    a, b = A[i]

    for x in range(X + 1):
        for y in range(Y + 1):
            if dp[i][x][y] == INF:
                continue

            dp[i + 1][x][y] = min(dp[i + 1][x][y], dp[i][x][y])

            nx = min(X, x + a)
            ny = min(Y, y + b)

            dp[i + 1][nx][ny] = min(dp[i + 1][nx][ny], dp[i][x][y] + 1)

if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
