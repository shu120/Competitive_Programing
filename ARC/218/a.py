from collections import defaultdict
import sys
input = sys.stdin.readline

MOD = 998244353
N, M = map(int, input().split())

cnt = defaultdict(dict)

for i in range(N):
    r = list(map(int, input().split()))

    r_cnt = defaultdict(int)
    for x in r:
        r_cnt[x] += 1

    for x, c in r_cnt.items():
        cnt[x][i] = c

total = pow(M, N, MOD)

ans = 0
pow_m = [1] * (N + 1)

for i in range(N):
    pow_m[i + 1] = pow_m[i] * M % MOD

for x in range(1, N * M + 1):
    rows = cnt[x]
    nc = 1
    used_rows = 0

    for c in rows.values():
        nc *= M - c
        nc %= MOD
        used_rows += 1

    nc *= pow_m[N - used_rows]
    nc %= MOD

    ans += total - nc
    ans %= MOD

print(ans)
