N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353

fact = [1] * (N + 1)
inv_fact = [1] * (N + 1)

for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[N] = pow(fact[N], MOD - 2, MOD)

for i in range(N, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD


def comb(n, r):
    if r < 0 or r > n:
        return 0

    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD


s = sum(A) % MOD
sq = sum(a * a for a in A) % MOD

ans = sq * comb(N - 1, K - 1)
ans += (s * s - sq) * comb(N - 2, K - 2)

print(ans % MOD)
