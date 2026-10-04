import sys
input = sys.stdin.readline

INF = 10**18
M = 500
T = int(input())

for _ in range(T):
    N = int(input())

    dp = [[INF] * M for _ in range(M)]

    for y in range(M):
        dp[0][y] = y * y

    spell = 0
    ans = 0

    for _ in range(N):
        X, Y, Z = map(int, input().split())

        spell += Z
        sword = INF

        for x in range(M):
            d = X - x
            cost = dp[x][Y] + d * d
            sword = min(sword, cost)

        curr = sword - Z
        ans = min(ans, curr)

        for y in range(M):
            d = Y - y
            cost = curr + d * d
            dp[X][y] = min(dp[X][y], cost)

    print(spell + ans)
