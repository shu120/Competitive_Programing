N, M = map(int, input().split())

row = [-1] * N
col = [-1] * N

ans = 0

for _ in range(M):
    R, C = map(int, input().split())
    R -= 1
    C -= 1

    if row[R] != -1:
        old_c = row[R]
        row[R] = -1
        col[old_c] = -1
        ans -= 1

    if col[C] != -1:
        old_r = col[C]
        col[C] = -1
        row[old_r] = -1
        ans -= 1

    row[R] = C
    col[C] = R
    ans += 1

print(ans)
