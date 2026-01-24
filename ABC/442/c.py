import sys
input = sys.stdin.readline

N, M = map(int, input().split())

deg = [0] * (N + 1)

for _ in range(M):
	A, B = map(int, input().split())
	deg[A] += 1
	deg[B] += 1

ans = []
for i in range(1, N + 1):
	u = N - 1 - deg[i]
	if u < 3:
		ans.append(0)
	else:
		ans.append(u * (u - 1) * (u - 2) // 6)

print(*ans)