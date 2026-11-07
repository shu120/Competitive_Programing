from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = [0] * (N + 1)
add = [None] * (N + 1)
order = []

for _ in range(M):
    A, B = map(int, input().split())

    cnt[A] += 1

    if add[A] is None:
        add[A] = defaultdict(int)

    add[A][B] += 1

for i in range(1, N + 1):
    order.append((-cnt[i], i))

order.sort()

ans = []

for k in range(1, N + 1):
    win = N + 1
    best = -1
    curr = add[k]

    if curr is not None:
        for j, val in curr.items():
            score = cnt[j] + val

            if score > best or score == best and j < win:
                best = score
                win = j

    for _, j in order:
        if j == k:
            continue

        if curr is not None and j in curr:
            continue

        if cnt[j] > best or cnt[j] == best and j < win:
            win = j
        break

    ans.append(str(win))

print("\n".join(ans))
