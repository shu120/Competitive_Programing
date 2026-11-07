N = int(input())
A = list(map(int, input().split()))

P = [0] * (N + 1)

for i in range(N):
    P[i + 1] = P[i] + A[i]

pre_min = [0] * (N + 1)
pre_max = [0] * (N + 1)
pre_min[0] = P[0]
pre_max[0] = P[0]

for i in range(N + 1):
    pre_min[i] = min(pre_min[i - 1], P[i])
    pre_max[i] = max(pre_max[i - 1], P[i])

suf_min = [0] * (N + 1)
suf_max = [0] * (N + 1)
suf_min[N] = P[N]
suf_max[N] = P[N]

for i in range(N - 1, -1, -1):
    suf_min[i] = min(suf_min[i + 1], P[i])
    suf_max[i] = max(suf_max[i + 1], P[i])

ans = pre_max[N] - pre_min[N] + 1

for i in range(N):
    high = max(pre_max[i], suf_max[i + 1] - 2 * A[i])
    low = min(pre_min[i], suf_min[i + 1] - 2 * A[i])

    ans = max(ans, high - low + 1)

print(ans)
