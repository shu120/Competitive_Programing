# C - Reorder cards
H, W, N = map(int, input().split())

row = []
col = []

for i in range(N):
    a, b = map(int, input().split())
    row.append((a, i))
    col.append((b, i))

row.sort()
col.sort()

ans_row = [0] * N
ans_col = [0] * N

curr = 0
prev = -1

for a, idx in row:
    if a != prev:
        curr += 1
        prev = a
    ans_row[idx] = curr

curr = 0
prev = -1

for b, idx in col:
    if b != prev:
        curr += 1
        prev = b
    ans_col[idx] = curr

for i in range(N):
    print(ans_row[i], ans_col[i])
