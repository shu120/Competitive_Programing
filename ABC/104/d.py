S = input()

MOD = 10**9 + 7

dp0 = 1
dp1 = 0
dp2 = 0
dp3 = 0

for c in S:
    if c == "A":
        dp1 += dp0

    elif c == "B":
        dp2 += dp1

    elif c == "C":
        dp3 += dp2

    else:
        old0 = dp0
        old1 = dp1
        old2 = dp2
        old3 = dp3

        dp0 = old0 * 3
        dp1 = old1 * 3 + old0
        dp2 = old2 * 3 + old1
        dp3 = old3 * 3 + old2

    dp0 %= MOD
    dp1 %= MOD
    dp2 %= MOD
    dp3 %= MOD

print(dp3)
