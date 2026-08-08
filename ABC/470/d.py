N, Q = map(int, input().split())
P = list(map(int, input().split()))

REV = [0] * N

for i in range(N):
    REV[P[i] - 1] = i + 1

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x = q[1] - 1
        y = q[2] - 1
        REV[P[x] - 1], REV[P[y] - 1] = y + 1, x + 1
        P[x], P[y] = P[y], P[x]

    else:
        P, REV = REV, P

print(*P)
