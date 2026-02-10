N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
total = 0

for b in B:
	sugar = A[b - 1]
	if sugar < K:
		cnt += 1
		total += sugar

print(cnt, total)