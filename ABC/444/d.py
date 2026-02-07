N = int(input())
A = list(map(int, input().split()))
A.sort()

maxA = A[-1]
res = []
carry = 0
idx = 0

for k in range(maxA):
	while idx < N and A[idx] <= k:
		idx += 1
	cnt = N - idx
	total = cnt + carry
	res.append(str(total % 10))
	carry = total // 10

while carry > 0:
	res.append(str(carry % 10))
	carry //= 10

print("".join(res[::-1]))