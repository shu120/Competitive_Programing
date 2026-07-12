import sys
from bisect import bisect_left

input = sys.stdin.readline


def solve(n: int, x: int, a: list[int]) -> int:
    mod = []
    minim = 10 ** 30

    for val in a:
        if val < minim:
            mod.append(val)
            minim = val

    size = len(mod)
    negative_mod = [-val for val in mod]
    full = [0] * size

    def calc(lim: int, start: int) -> int:
        rslt = 0

        while lim > 0:
            idx = bisect_left(negative_mod, -lim, lo=start)

            if idx == size:
                return rslt + 1

            rslt += (lim // mod[idx]) * full[idx]

            lim %= mod[idx]
            start = idx + 1

        return rslt

    full[-1] = 1

    for idx in range(size - 2, -1, -1):
        full[idx] = calc(mod[idx], idx + 1)

    return calc(x + 1, 0) - 1


T = int(input())
ans = []

for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans.append(str(solve(N, X, A)))

print("\n".join(ans))
