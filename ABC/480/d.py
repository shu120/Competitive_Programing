import sys
from bisect import bisect_left
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N + 1)

for i in range(N):
    S[i + 1] = S[i] + A[i]

T = [0] * (N + 1)

for i in range(1, N + 1):
    T[i] = T[i - 1] + S[i]

leng = [0] * (N + 1)

for i in range(1, N + 1):
    leng[i] = leng[i - 1] + i

for _ in range(Q):
    L, R = map(int, input().split())

    i = bisect_left(leng, R)
    rem = R - leng[i - 1]
    right = T[i - 1] + S[rem]

    if L - 1 == 0:
        left = 0
    else:
        i = bisect_left(leng, L - 1)
        rem = (L - 1) - leng[i - 1]
        left = T[i - 1] + S[rem]

    print(right - left)
