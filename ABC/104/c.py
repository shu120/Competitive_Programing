# C - All Green
D, G = map(int, input().split())

PC = []
for _ in range(D):
    p, c = map(int, input().split())
    PC.append((p, c))

ans = 10**9

for bit in range(1 << D):
    total = 0
    count = 0

    for i in range(D):
        p, c = PC[i]
        score = (i + 1) * 100

        if bit & (1 << i):
            total += p * score + c
            count += p

    if total < G:
        for i in range(D - 1, -1, -1):
            if bit & (1 << i):
                continue

            p, c = PC[i]
            score = (i + 1) * 100

            need = G - total
            solve = min(p - 1, (need + score - 1) // score)

            total += solve * score
            count += solve

            break

    if total >= G:
        ans = min(ans, count)

print(ans)
