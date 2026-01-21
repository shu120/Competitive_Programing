import sys

it = iter(sys.stdin.read().split())
H = int(next(it))
W = int(next(it))
N = int(next(it))

A = [[int(next(it)) for _ in range(W)] for _ in range(H)]
Bset = {int(next(it)) for _ in range(N)}

ans = 0
for row in A:
	cnt = 0
	for x in row:
		if x in Bset:
			cnt += 1
	ans = max(ans, cnt)

print(ans)
