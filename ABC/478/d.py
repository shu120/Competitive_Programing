N, Q = map(int, input().split())

e = [[] for _ in range(N + 2)]
ans = []

for _ in range(Q):
    L, R, X = map(int, input().split())
    e[L].append((X, 1))
    e[R + 1].append((X, -1))

cnt = {}
kind = 0

for i in range(1, N + 1):
    for X, d in e[i]:
        before = cnt.get(X, 0)
        cnt[X] = before + d

        if before == 0 and cnt[X] > 0:
            kind += 1
        elif before > 0 and cnt[X] == 0:
            kind -= 1

    ans.append(kind)

print(*ans)
