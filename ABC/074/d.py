#D - Restoring Road Network
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N):
	for j in range(i + 1, N):
		need = True
		for k in range(N):
			if k == i or k == j:
				continue

			if A[i][j] > A[i][k] + A[k][j]:
				print(-1)
				exit()

			if A[i][j] == A[i][k] + A[k][j]:
				need = False

		if need:
			ans += A[i][j]

print(ans)