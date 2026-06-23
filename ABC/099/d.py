#D - Good Grid
N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]

count = [[0] * C for _ in range(3)]

for i in range(N):
    for j in range(N):
        color = grid[i][j] - 1
        group = (i + j) % 3
        count[group][color] += 1

cost = [[0] * C for _ in range(3)]

for group in range(3):
    for new_color in range(C):
        total = 0
        for old_color in range(C):
            total += count[group][old_color] * D[old_color][new_color]
        cost[group][new_color] = total

ans = 10**18

for c0 in range(C):
    for c1 in range(C):
        for c2 in range(C):
            if c0 == c1 or c1 == c2 or c2 == c0:
                continue

            total = cost[0][c0] + cost[1][c1] + cost[2][c2]
            ans = min(ans, total)

print(ans)
