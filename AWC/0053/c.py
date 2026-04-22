from collections import defaultdict

N = int(input())
diff = defaultdict(int)

for _ in range(N):
    X, L, R, C = map(int, input().split())
    left = X - L
    right = X + R
    diff[left] += C
    diff[right + 1] -= C

cur = 0
ans = 0

for pos in sorted(diff):
    cur += diff[pos]
    ans = max(ans, cur)

print(ans)
