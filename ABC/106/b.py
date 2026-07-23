#B - 105
N = int(input())

ans = 0
for i in range(1, N + 1, 2):
    d = 0
    for j in range(1, i + 1):
        if i % j == 0:
            d += 1
    if d == 8:
        ans += 1
print(ans)
