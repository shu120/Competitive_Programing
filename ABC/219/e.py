# E - Moat
from collections import deque

A = [list(map(int, input().split())) for _ in range(4)]

ans = 0

for bit in range(1 << 16):
    ok = True

    for i in range(4):
        for j in range(4):
            if A[i][j] == 1:
                k = i * 4 + j
                if not (bit >> k & 1):
                    ok = False

    if not ok:
        continue

    ins = []

    for i in range(4):
        for j in range(4):
            k = i * 4 + j
            if bit >> k & 1:
                ins.append((i, j))

    q = deque([ins[0]])
    seen = {ins[0]}

    while q:
        i, j = q.popleft()

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = i + di
            nj = j + dj

            if not (0 <= ni < 4 and 0 <= nj < 4):
                continue

            k = ni * 4 + nj

            if not (bit >> k & 1):
                continue

            if (ni, nj) in seen:
                continue

            seen.add((ni, nj))
            q.append((ni, nj))

    if len(seen) != len(ins):
        continue

    q = deque([(-1, -1)])
    seen = {(-1, -1)}

    while q:
        i, j = q.popleft()

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = i + di
            nj = j + dj

            if not (-1 <= ni <= 4 and -1 <= nj <= 4):
                continue

            if 0 <= ni < 4 and 0 <= nj < 4:
                k = ni * 4 + nj

                if bit >> k & 1:
                    continue

            if (ni, nj) in seen:
                continue

            seen.add((ni, nj))
            q.append((ni, nj))

    ok = True

    for i in range(4):
        for j in range(4):
            k = i * 4 + j

            if not (bit >> k & 1):
                if (i, j) not in seen:
                    ok = False

    if not ok:
        continue

    ans += 1

print(ans)
