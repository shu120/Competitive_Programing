from bisect import bisect_right

N = int(input())

H = []
L = []

for _ in range(N):
    h, _l = map(int, input().split())
    H.append(h)
    L.append(_l)

Q = int(input())
T = list(map(int, input().split()))

sfx_max = [0] * (N + 1)

for i in reversed(range(N)):
    sfx_max[i] = max(sfx_max[i + 1], H[i])

for t in T:
    idx = bisect_right(L, t)
    print(sfx_max[idx])
