H, W, Q = map(int, input().split())

char = ["A"] * (Q + 1)

best = [[0] * (W + 1) for _ in range(H + 1)]

for k in range(1, Q + 1):
    R, C, X = input().split()
    R = int(R) - 1
    C = int(C) - 1

    char[k] = X

    if best[R][C] < k:
        best[R][C] = k

for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        best[i][j] = max(
            best[i][j],
            best[i + 1][j],
            best[i][j + 1]
        )

for i in range(H):
    row = []
    for j in range(W):
        row.append(char[best[i][j]])
    print("".join(row))
