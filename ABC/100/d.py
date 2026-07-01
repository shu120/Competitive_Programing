#D - Patisserie ABC

N, M = map(int, input().split())

cakes = []
for _ in range(N):
    x, y, z = map(int, input().split())
    cakes.append((x, y, z))

ans = 0

for sx in [1, -1]:
    for sy in [1, -1]:
        for sz in [1, -1]:
            score = []

            for x, y, z in cakes:
                scr = sx * x + sy * y + sz * z
                score.append(scr)

            score.sort(reverse=True)

            total = sum(score[:M])
            ans = max(ans, total)

print(ans)
