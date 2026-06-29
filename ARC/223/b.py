import sys
input = sys.stdin.readline

MOD = 998244353

T = int(input())

MAX_N = 2 * 10 ** 5

fact = [1] * (MAX_N + 1)
inv_fact = [1] * (MAX_N + 1)

for i in range(1, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[MAX_N] = pow(fact[MAX_N], MOD - 2, MOD)

for i in range(MAX_N, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    rem = []
    key = []

    for a in A:
        r = a % K
        rem.append(r)
        key.append(min(r, (-r) % K))

    res = 1
    l_ = 0

    while l_ < N:
        r = l_

        while r < N and key[r] == key[l_]:
            r += 1

        length = r - l_
        cur_key = key[l_]

        if (2 * cur_key) % K == 0:
            res *= fact[length]
            res %= MOD

            cnt = {}

            for i in range(l_, r):
                cnt[A[i]] = cnt.get(A[i], 0) + 1

            for c in cnt.values():
                res *= inv_fact[c]
                res %= MOD

        else:
            c = 0

            for i in range(l_, r):
                if rem[i] == cur_key:
                    c += 1

            res *= fact[length]
            res %= MOD
            res *= inv_fact[c]
            res %= MOD
            res *= inv_fact[length - c]
            res %= MOD

        l_ = r

    print(res)
