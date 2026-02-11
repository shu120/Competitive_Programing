N = int(input())

L = []
R = []

for _ in range(N):
	l, r = input().split()
	L.append(l)
	R.append(r)

ans = 0
for i in range(N - 1):
	if R[i] == L[i + 1]:
		ans += 1

print(ans)