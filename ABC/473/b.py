from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

ans = 0

for x, c in cnt.items():
    if c % 2 == 1:
        ans += x

print(ans)
