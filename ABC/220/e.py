# E - Distance on Large Perfect Binary Tree
N, D = map(int, input().split())
MOD = 998244353

pow2 = [1] * (N + D + 1)

for i in range(1, len(pow2)):
    pow2[i] = pow2[i - 1] * 2 % MOD

ans = 0

for h in range(N):
    height = N - 1 - h

    left = max(0, D - height)
    right = min(D, height)

    if left > right:
        continue

    cnt = right - left + 1
    mid = cnt

    if left == 0:
        mid -= 1

    if right == D:
        mid -= 1

    way = mid * pow2[D - 1] if D >= 1 else 0

    if left == 0:
        way += pow2[D]

    if right == D and D != 0:
        way += pow2[D]

    ans += pow2[h] * way
    ans %= MOD

print(ans)
