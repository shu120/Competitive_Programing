#C - Write and Erase
from collections import Counter

N = int(input())
A = [input() for _ in range(N)]

a = Counter(A)

ans = 0
for i in a.values():
	if i % 2 == 1:
		ans += 1

print(ans)