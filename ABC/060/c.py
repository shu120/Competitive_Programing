N, T = map(int, input().split())
t = list(map(int, input().split()))

total = T
for i in range(N - 1):
	total += min(T, t[i + 1] - t[i])

print(total)