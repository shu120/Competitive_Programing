# D - Equal Cut
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

presum = [0] * (N + 1)
for i in range(N):
    presum[i + 1] = presum[i] + A[i]

ans = 10**30

for j in range(2, N - 1):
    left_total = presum[j]
    i = bisect_left(presum, left_total / 2, 1, j)

    left_cand = []
    for ni in [i - 1, i]:
        if 1 <= ni < j:
            P = presum[ni]
            Q = presum[j] - presum[ni]
            left_cand.append((P, Q))

    right_total = presum[N] - presum[j]
    target = presum[j] + right_total / 2
    k = bisect_left(presum, target, j + 1, N)

    right_cand = []
    for nk in [k - 1, k]:
        if j < nk < N:
            R = presum[nk] - presum[j]
            S_ = presum[N] - presum[nk]
            right_cand.append((R, S_))

    for P, Q in left_cand:
        for R, S_ in right_cand:
            ans = min(ans, max(P, Q, R, S_) - min(P, Q, R, S_))

print(ans)
