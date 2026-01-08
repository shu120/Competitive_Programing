#ABC067 C - Splitting Pile
from itertools import accumulate
N = int(input())
a = list(map(int, input().split()))

presum = list(accumulate(a))
s = presum[-1]

ans = 10 ** 18
for i in range(N - 1):
	diff = abs(2 * presum[i] - s)
	if diff < ans:
		ans = diff

print(ans)