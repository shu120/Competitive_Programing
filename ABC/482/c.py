from bisect import bisect_left, bisect_right

H, W, N, Q = map(int, input().split())

row = []
col = []

for _ in range(N):
    R, C = map(int, input().split())
    row.append(R)
    col.append(C)

row.sort(), col.sort()

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        ans = bisect_right(row, q[2]) - bisect_left(row, q[1])
    else:
        ans = bisect_right(col, q[2]) - bisect_left(col, q[1])

    print(ans)
