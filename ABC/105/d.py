# D - Candy Distribution
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
cnt[0] = 1

s = 0
ans = 0

for a in A:
    s = (s + a) % M
    ans += cnt[s]
    cnt[s] += 1

print(ans)
