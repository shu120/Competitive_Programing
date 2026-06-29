import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())

    w = [0] * (N + 1)
    v = [0] * (N + 1)

    for i in range(1, N + 1):
        w[i], v[i] = map(int, input().split())

    sum_w = [0] * (N + 1)
    sum_v = [0] * (N + 1)

    for i in range(1, N + 1):
        sum_w[i] = sum_w[i - 1] + w[i]
        sum_v[i] = sum_v[i - 1] + v[i]

    i = N
    cap = W
    val = 0
    best = 0

    while i >= 1:
        if cap >= sum_w[i]:
            best = max(best, val + sum_v[i])
            break

        if cap < w[i]:
            i -= 1
            continue

        best = max(best, val + sum_v[i - 1])

        val += v[i]
        cap -= w[i]
        i -= 1

    best = max(best, val)
    print(best)
