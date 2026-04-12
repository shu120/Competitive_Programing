#C - Shopping Street
import sys
input = sys.stdin.readline

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -10**30

for mask in range(1, 1 << 10):
    profit = 0

    for i in range(N):
        cnt = 0
        for j in range(10):
            if (mask >> j)&1 and F[i][j]:
                cnt += 1
        profit += P[i][cnt]

    ans = max(ans, profit)

print(ans)
