MOD = 998244353

N = input().strip()
D = 10

dp = [[[[0 for _ in range(2)] for _ in range(3)] for _ in range(1 << D)] for _ in range(len(N) + 1)]

dp[0][0][0][0] = 1

for i in range(len(N)):
    si = int(N[i])

    for b in range(1 << D):
        for m in range(3):
            for smaller in range(2):
                now = dp[i][b][m][smaller]
                if now == 0:
                    continue

                for d in range(10):
                    if smaller == 0 and d > si:
                        continue

                    if b == 0 and d == 0:
                        nb = 0
                    else:
                        nb = b | (1 << d)

                    nm = (m * 10 + d) % 3

                    if smaller == 1:
                        ns = 1
                    else:
                        ns = 0 if d == si else 1

                    dp[i + 1][nb][nm][ns] += now
                    dp[i + 1][nb][nm][ns] %= MOD

ans = 0

for b in range(1, 1 << D):
    for m in range(3):
        for smaller in range(2):
            cond = 0

            if b.bit_count() == 3:
                cond += 1

            if b & (1 << 3):
                cond += 1

            if m == 0:
                cond += 1

            if cond == 1:
                ans += dp[len(N)][b][m][smaller]
                ans %= MOD

print(ans)
