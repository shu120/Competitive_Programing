N, M = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

C.sort()
R.sort()

i = 0
j = 0
ans = 0

while i < N and j < M:
	if C[i] <= R[j]:
		ans += 1
		i += 1
		j += 1
	else:
		j += 1

print(ans)