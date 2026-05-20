import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def sum_prefix(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum(self, l, r):
        return self.sum_prefix(r) - self.sum_prefix(l)


N, M = map(int, input().split())

P1 = [[] for _ in range(N)]
P2 = [[] for _ in range(N)]
intervals = []

for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    P1[l].append(r)
    P2[r].append(l)
    intervals.append((l, r))

for i in range(N):
    P1[i].sort()
    P2[i].sort()

intervals.sort(key=lambda x: -x[0])

Qn = int(input())

queries = []
for i in range(Qn):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    queries.append((s, t, i))

queries.sort(key=lambda x: -x[0])

fw = FenwickTree(N)
now = 0
ans = ["No"] * Qn

for s, t, qi in queries:
    while now < M and intervals[now][0] >= s:
        fw.add(intervals[now][1], 1)
        now += 1

    rs = P1[s]
    lidx = bisect_right(rs, t)

    if lidx == 0:
        ans[qi] = "No"
        continue

    lm = rs[lidx - 1]

    ls = P2[t]
    ridx = bisect_left(ls, s)

    if ridx == len(ls):
        ans[qi] = "No"
        continue

    rm = ls[ridx]

    if lm == t:
        if fw.sum(s, t + 1) >= 2:
            ans[qi] = "Yes"
        else:
            ans[qi] = "No"

    elif lm + 1 >= rm:
        ans[qi] = "Yes"

    else:
        ans[qi] = "No"

print("\n".join(ans))
