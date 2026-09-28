# E - Integers on Grid
H, W, N = map(int, input().split())

cell = []
for i in range(N):
    r, c, a = map(int, input().split())
    r -= 1
    c -= 1
    cell.append((a, r, c, i))

cell.sort(reverse=True)

row_best = [0] * H
col_best = [0] * W
ans = [0] * N

i = 0

while i < N:
    j = i

    while j < N and cell[j][0] == cell[i][0]:
        j += 1

    for k in range(i, j):
        a, r, c, idx = cell[k]
        ans[idx] = max(row_best[r], col_best[c])

    for k in range(i, j):
        a, r, c, idx = cell[k]
        val = ans[idx] + 1
        row_best[r] = max(row_best[r], val)
        col_best[c] = max(col_best[c], val)

    i = j

for x in ans:
    print(x)
