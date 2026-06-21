#D - Static Sushi
N, C = map(int, input().split())

x = [0] * N
v = [0] * N
for i in range(N):
    x[i], v[i] = map(int, input().split())

cw = [0] * N
cw_back = [0] * N

s = 0
for i in range(N):
    s += v[i]
    cw[i] = s - x[i]
    cw_back[i] = s - 2 * x[i]

ccw = [0] * N
ccw_back = [0] * N

s = 0
for i in range(N - 1, -1, -1):
    s += v[i]
    dist = C - x[i]
    ccw[i] = s - dist
    ccw_back[i] = s - 2 * dist

cw_best = [0] * N
cw_back_best = [0] * N

cw_best[0] = cw[0]
cw_back_best[0] = cw_back[0]

for i in range(1, N):
    cw_best[i] = max(cw_best[i - 1], cw[i])
    cw_back_best[i] = max(cw_back_best[i - 1], cw_back[i])

ccw_best = [0] * N
ccw_back_best = [0] * N

ccw_best[N - 1] = ccw[N - 1]
ccw_back_best[N - 1] = ccw_back[N - 1]

for i in range(N - 2, -1, -1):
    ccw_best[i] = max(ccw_best[i + 1], ccw[i])
    ccw_back_best[i] = max(ccw_back_best[i + 1], ccw_back[i])

ans = 0

ans = max(ans, cw_best[N - 1])

ans = max(ans, ccw_best[0])

for i in range(N - 1):
    ans = max(ans, cw_back_best[i] + ccw_best[i + 1])

for i in range(1, N):
    ans = max(ans, ccw_back_best[i] + cw_best[i - 1])

print(ans)
