#TLE
import math

MOD = 998244353

def lcm(a, b):
	return a // math.gcd(a, b) * b

def solve(A):
	N = len(A)
	out = []
	for k in range(N):
		L = 1
		for i in range(N):
			if i == k:
				continue
			L = lcm(L, A[i])
		out.append(L % MOD)
	return out

T = int(input())
for _ in range(T):
	N = int(input())
	A = list(map(int, input().split()))
	print(*solve(A))