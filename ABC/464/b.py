H, W = map(int, input().split())
C = [input() for _ in range(H)]

rows = []
for i in range(H):
    if "#" in C[i]:
        rows.append(i)

cols = []
for j in range(W):
    black = False
    for i in range(H):
        if C[i][j] == "#":
            black = True
    if black:
        cols.append(j)

for i in range(rows[0], rows[-1] + 1):
    ans = ""
    for j in range(cols[0], cols[-1] + 1):
        ans += C[i][j]
    print(ans)
