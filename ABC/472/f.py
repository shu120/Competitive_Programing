# TLE
N, Q = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    poli = []

    curr = u

    while True:
        poli.append(P[curr])

        if curr == v:
            break

        curr = (curr + 1) % N

    s = 0
    sx = 0
    sy = 0

    m = len(poli)

    for i in range(m):
        x1, y1 = poli[i]
        x2, y2 = poli[(i + 1) % m]

        cross = x1 * y2 - x2 * y1

        s += cross
        sx += (x1 + x2) * cross
        sy += (y1 + y2) * cross

    cx = sx / (3 * s)
    cy = sy / (3 * s)

    print(cx, cy)
