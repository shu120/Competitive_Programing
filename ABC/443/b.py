N, K = map(int, input().split())

total = 0
ans = 0

while total < K:
	total += N
	N += 1
	ans += 1

print(ans - 1)