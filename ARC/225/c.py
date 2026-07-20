#C - K Spanning Tree
import sys
from atcoder.dsu import DSU
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    N, M, K = map(int, input().split())

    zero = []
    one = []

    for idx in range(1, M + 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1

        if c == 0:
            zero.append((a, b, idx))
        else:
            one.append((a, b, idx))

    uf = DSU(N)

    for a, b, idx in zero:
        uf.merge(a, b)

    must = []

    for a, b, idx in one:
        if not uf.same(a, b):
            uf.merge(a, b)
            must.append((a, b, idx))

    if len(must) > K:
        out.append("-1")
        continue

    uf = DSU(N)
    ans = []

    for a, b, idx in must:
        uf.merge(a, b)
        ans.append(idx)

    for a, b, idx in one:
        if len(ans) == K:
            break

        if not uf.same(a, b):
            uf.merge(a, b)
            ans.append(idx)

    if len(ans) < K:
        out.append("-1")
        continue

    for a, b, idx in zero:
        if not uf.same(a, b):
            uf.merge(a, b)
            ans.append(idx)

    out.append(" ".join(map(str, ans)))

print("\n".join(out))
