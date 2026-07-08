#D - Islands War
N, M = map(int, input().split())

BA = []
for _ in range(M):
    a, b = map(int, input().split())
    BA.append((b, a))

BA.sort()

ans = 0
last = 0

for b, a in BA:
    if last < a:
        ans += 1
        last = b - 1

print(ans)
