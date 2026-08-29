N, K = map(int, input().split())
A = list(map(int, input().split()))

best = {}
best[0] = 0

s = 0
dp = 0
mx = 0

for a in A:
    s += a
    s %= K

    ndp = mx

    if s in best:
        ndp = max(ndp, best[s] + 1)

    if s not in best:
        best[s] = ndp
    else:
        best[s] = max(best[s], ndp)

    dp = ndp
    mx = max(mx, dp)

print(dp)
