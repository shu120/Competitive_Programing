#D
from collections import defaultdict

n, m = map(int, input().split())
a = input().split()

pow = {L: pow(10, L, m) for L in range(1, 11)}
mod = {L: defaultdict(int) for L in pow}

for i in a:
	L = len(i)
	mod[L][int(i) % m] += 1

ans = 0

for i in a:
	val_a = int(i)
	for L in pow:
		n = (-val_a * pow[L]) % m
		ans += mod[L][n]

print(ans)