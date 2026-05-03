dice = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
for a in dice[0]:
    for b in dice[1]:
        for c in dice[2]:
            if sorted([a, b, c]) == ([4, 5, 6]):
                cnt += 1

print(cnt / 216)
