# F - Problem where +s Separate Digits
S = input()
MOD = 998244353

total = int(S[0])
last = int(S[0])
cnt = 1

for c in S[1:]:
    x = int(c)

    new_total = (2 * total + 9 * last + 2 * cnt * x ) % MOD

    new_last = (10 * last + 2 * cnt * x ) % MOD

    total = new_total
    last = new_last
    cnt = cnt * 2 % MOD

print(total)
