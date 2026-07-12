import sys

input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    a = [-1] * N
    st = [(0, -1)]

    while st:
        v, p = st.pop()

        if a[v] != -1:
            continue

        if p == -1:
            a[v] = 0
        else:
            a[v] = a[p] + 1

        for nv in g[v]:
            if a[nv] == -1:
                st.append((nv, v))

    ans.append(" ".join(map(str, a)))

print("\n".join(ans))
