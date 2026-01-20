#C - Together
from collections import Counter

N = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)

ans = 0
for x in cnt.keys():
	v = cnt[x - 1] + cnt[x] + cnt[x + 1]
	if v > ans:
		ans = v

print(ans)