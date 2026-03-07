N ,M = map(int, input().split())
C = list(map(int, input().split()))

sum_B = [0] * M

for _ in range(N):
	A, B = map(int, input().split())
	sum_B[A - 1] += B

ans = 0
for j in range(M):
	ans += min(C[j], sum_B[j])

print(ans)