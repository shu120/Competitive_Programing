# TLE
# まじでどうすんねんこれ意味わからん
import sys
input = sys.stdin.readline

INF = 10**30
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
            cost = dp[x][Y] + (X - x) ** 2
            sword = min(sword, cost)

        curr = sword - Z
        ans = min(ans, curr)

        for y in range(M):
            cost = curr + (Y - y) ** 2
            dp[X][y] = min(dp[X][y], cost)

    print(spell + ans)
