import math
N = int(input())

def digits(x):
	return len(str(x))

ans = digits(N)

for a in range(1, int(math.isqrt(N)) + 1):
	if N % a == 0:
		b = N // a
		ans = min(ans, max(digits(a), digits(b)))

print(ans)
