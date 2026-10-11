import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
INF = 10 ** 18

L = [INF, INF] + list(map(int, input().split()))
R = [INF] + list(map(int, input().split())) + [INF]

l_R = [INF] * (N + 1)
r_L = [INF] * (N + 2)

for i in range(1, N + 1):
    l_R[i] = min(l_R[i - 1], R[i])

for i in range(N, 0, -1):
    r_L[i] = min(r_L[i + 1], L[i])

for _ in range(Q):
    s, t = map(int, input().split())

    if s < t:
        print(min(R[s], L[s] + l_R[s - 1]))
    else:
        print(min(L[s], R[s] + r_L[s + 1]))
