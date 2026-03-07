import sys
input = sys.stdin.buffer.readline

K, M = map(int, input().split())
MOD = M * 10007
MOD9 = MOD * 9

x = 0
for _ in range(K):
	c, l = map(int, input().split())
	p = pow(10, l, MOD)
	rep = (pow(10, l, MOD9) - 1) // 9 % MOD
	x = (x * p + c * rep) % MOD

print((x // M) % 10007)