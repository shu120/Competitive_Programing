N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
x = 0

for a in A:
	if a >= x:
		ans += a - x
		x = a + 100

if x < T:
	ans += T - x

print(ans)