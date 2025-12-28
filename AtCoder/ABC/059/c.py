def solve(a, first):
	total = 0
	cost = 0

	for i in range(len(a)):
		total += a[i]

		expected = first if i % 2 == 0 else -first

		if total * expected <= 0:
			cost += abs(total - expected)
			total = expected
	
	return cost

n = int(input())
a = list(map(int, input().split()))

print(min(solve(a, 1), solve(a, -1)))
