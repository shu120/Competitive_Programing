#D - Axis-Parallel Rectangle
N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

ans = float('inf')

for i in range(N):
    for j in range(N):
        sx = points[i][0]
        tx = points[j][0]
        if sx > tx:
            sx, tx = tx, sx

        for k in range(N):
            for m in range(N):
                sy = points[k][1]
                ty = points[m][1]
                if sy > ty:
                    sy, ty = ty, sy

                cnt = 0
                for x, y in points:
                    if sx <= x <= tx and sy <= y <= ty:
                        cnt += 1

                if cnt >= K:
                    area = (tx - sx) * (ty - sy)
                    ans = min(ans, area)

print(ans)
