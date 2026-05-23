import sys
input = sys.stdin.readline

MOD = 998244353

N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

children = [[] for _ in range(N)]

for i, p in enumerate(P, start=1):
    p -= 1
    children[p].append(i)

max_d = sum(D)

fact = [1] * (max_d + 1)
invfact = [1] * (max_d + 1)

for i in range(1, max_d + 1):
    fact[i] = fact[i - 1] * i % MOD

invfact[max_d] = pow(fact[max_d], MOD - 2, MOD)

for i in range(max_d, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def comb_large_n(n, k):
    if n < k:
        return 0

    res = 1
    for i in range(k):
        res *= (n - i) % MOD
        res %= MOD

    res *= invfact[k]
    res %= MOD

    return res


order = []
stack = [0]

while stack:
    v = stack.pop()
    order.append(v)

    for nv in children[v]:
        stack.append(nv)

surplus = [0] * N
ans = 1

for v in reversed(order):
    available = C[v]

    for nv in children[v]:
        available += surplus[nv]

    if available < D[v]:
        print(0)
        exit()

    ans *= comb_large_n(available, D[v])
    ans %= MOD

    surplus[v] = available - D[v]

print(ans)
