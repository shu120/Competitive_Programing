N, K = map(int, input().split())

total = 0
disc = []

for _ in range(N):
	A, B = map(int, input().split())
	total += A
	disc.append(A - B)

disc.sort(reverse=True)

for i in range(min(K, N)):
	total -= disc[i]

print(total)