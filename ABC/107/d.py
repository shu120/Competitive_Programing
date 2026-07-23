#D - Median of Medians
from atcoder.fenwicktree import FenwickTree

N = int(input())
A = list(map(int, input().split()))

val = sorted(set(A))

total = N * (N + 1) // 2
need = (total + 1) // 2


def check(x):
    bit = FenwickTree(2 * N + 1)

    s = 0
    cnt = 0
    offset = N

    bit.add(offset, 1)

    for a in A:
        if a >= x:
            s += 1
        else:
            s -= 1

        idx = s + offset

        cnt += bit.sum(0, idx + 1)
        bit.add(idx, 1)

    return cnt >= need


ok = 0
ng = len(val)

while ng - ok > 1:
    mid = (ok + ng) // 2

    if check(val[mid]):
        ok = mid
    else:
        ng = mid

print(val[ok])
