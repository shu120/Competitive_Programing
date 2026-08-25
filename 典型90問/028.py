#028 - Cluttered Paper（★4）
N = int(input())

SIZE = 1001
imos = [[0] * SIZE for _ in range(SIZE)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())

    imos[lx][ly] += 1
    imos[rx][ly] -= 1
    imos[lx][ry] -= 1
    imos[rx][ry] += 1

for x in range(SIZE - 1):
    for y in range(SIZE):
        imos[x + 1][y] += imos[x][y]

for x in range(SIZE):
    for y in range(SIZE - 1):
        imos[x][y + 1] += imos[x][y]

ans = [0] * (N + 1)

for x in range(1000):
    for y in range(1000):
        k = imos[x][y]

        if k > 0:
            ans[k] += 1

for k in range(1, N + 1):
    print(ans[k])
