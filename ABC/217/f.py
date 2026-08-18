# F - Make Pair
N, M = map(int, input().split())
MOD = 998244353

size = 2 * N

nakayoshi = [[False] * size for _ in range(size)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    nakayoshi[A][B] = True
    nakayoshi[B][A] = True

comb = [[0] * (N + 1) for _ in range(N + 1)]

for n in range(N + 1):
    comb[n][0] = 1

    for r in range(1, n + 1):
        comb[n][r] = (comb[n - 1][r - 1] + comb[n - 1][r]) % MOD

dp = [[0] * (size + 1) for _ in range(size + 1)]

for i in range(size + 1):
    dp[i][i] = 1

for leng in range(2, size + 1, 2):
    for le in range(size - leng + 1):
        ri = le + leng

        for partner in range(le + 1, ri, 2):
            if not nakayoshi[le][partner]:
                continue

            ins = dp[le + 1][partner]
            outs = dp[partner + 1][ri]

            ins_pair = (partner - le + 1) // 2
            total_pair = leng // 2

            way = ins * outs % MOD
            way *= comb[total_pair][ins_pair]
            way %= MOD

            dp[le][ri] += way
            dp[le][ri] %= MOD

print(dp[0][size])
