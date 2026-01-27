import sys
input = sys.stdin.readline

N = int(input())
S = [input() for _ in range(N)]

def makecost(row, N):
	pref = [0] * (N + 1)
	for j in range(N):
		pref[j + 1] = pref[j] + (row[j] == '#')
	total = pref[N]

	cost = [0] * (N + 1)
	for k in range(N + 1):
		hash_prefix = pref[k]
		hash_suffix = total - pref[k]
		dot_suffix = (N - k) - hash_suffix
		cost[k] = hash_prefix + dot_suffix
	return cost

dp_base = makecost(S[0], N)

for i in range(1, N):
	suf_min = [0] * (N + 2)
	suf_min[N] = dp_base[N]
	for k in range(N - 1, -1, -1):
		a = dp_base[k]
		b = suf_min[k + 1]
		suf_min[k] = min(a, b)

	cost = makecost(S[i], N)
	dp_curr = [0] * (N + 1)
	for k in range(N + 1):
		dp_curr[k] = cost[k] + suf_min[k]

	dp_base = dp_curr

print(min(dp_base))