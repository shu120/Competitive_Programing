import sys
input = sys.stdin.readline

L, R, D, U = map(int, input().split())

def f(k):
	x1 = max(L, -k)
	x2 = min(R,  k)
	y1 = max(D, -k)
	y2 = min(U,  k)
	if x1 > x2 or y1 > y2:
		return 0
	return (x2 - x1 + 1) * (y2 - y1 + 1)

K = max(abs(L), abs(R), abs(D), abs(U))
ans = 0
prev = 0

for k in range(K + 1):
	curr = f(k)
	if k % 2 == 0:
		ans += curr - prev
	prev = curr

print(ans)
