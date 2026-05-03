S = input()
MOD = 998244353

ans = 0
curr = 0

for i in range(len(S)):
    if i == 0:
        curr = 1
    else:
        if S[i] != S[i - 1]:
            curr += 1
        else:
            curr = 1

    ans += curr

print(ans % MOD)
