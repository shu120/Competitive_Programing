#C
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

dif = Y - X
first = A[0]
low = float('-inf')
high = float('inf')
sum_a = 0

for i in A:
	num = (first - i) * X
	if num % dif != 0:
		print (-1)
		exit ()
	a = num // dif
	sum_a += a
	low = max(low, -a)
	high = min(high, i - a)

if low > high:
	print(-1)
	exit()

print(N * int(high) + sum_a)