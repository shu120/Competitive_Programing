from atcoder.dsu import DSU
from collections import defaultdict

N, M = map(int, input().split())
S = input()

MOD = 998244353

uf = DSU(N)

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    uf.merge(A, B)

fact = [1] * (N + 1)
inv_fact = [1] * (N + 1)

for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[N] = pow(fact[N], MOD - 2, MOD)

for i in range(N, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

cnt = defaultdict(int)

for i, c in enumerate(S):
    r = uf.leader(i)
    cnt[(r, c)] += 1

ways = 1
dup = False

for i in range(N):
    if uf.leader(i) == i:
        ways *= fact[uf.size(i)]
        ways %= MOD

for num in cnt.values():
    ways *= inv_fact[num]
    ways %= MOD

    if num >= 2:
        dup = True

if dup:
    ans = ways
else:
    ans = ways * pow(2, MOD - 2, MOD) % MOD

print(ans)
