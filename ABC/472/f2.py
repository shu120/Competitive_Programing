N, Q = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

area = [0] * (2 * N + 1)
sx = [0] * (2 * N + 1)
sy = [0] * (2 * N + 1)

for i in range(2 * N):
    x1, y1 = P[i % N]
    x2, y2 = P[(i + 1) % N]
    cross = x1 * y2 - x2 * y1

    area[i + 1] = area[i] + cross
    sx[i + 1] = sx[i] + (x1 + x2) * cross
    sy[i + 1] = sy[i] + (y1 + y2) * cross

for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    if v < u:
        v += N

    s = area[v] - area[u]
    x_sum = sx[v] - sx[u]
    y_sum = sy[v] - sy[u]

    x1, y1 = P[v % N]
    x2, y2 = P[u]
    cross = x1 * y2 - x2 * y1

    s += cross
    x_sum += (x1 + x2) * cross
    y_sum += (y1 + y2) * cross

    cx = x_sum / (3 * s)
    cy = y_sum / (3 * s)

    print(cx, cy)
