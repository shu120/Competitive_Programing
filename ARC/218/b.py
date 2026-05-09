from collections import Counter
import sys
input = sys.stdin.readline


def apply(size: int, grundy: int) -> int:
    if size == 0:
        return grundy
    if size <= grundy:
        return size - 1
    return size


def solve() -> str:
    N = int(input())
    A = list(map(int, input().split()))

    counter = Counter(A)
    val = sorted(counter.keys())

    parts = []
    prev = 0

    for v in val:
        gap = v - prev
        parts.append(gap)
        parts.append(counter[v])
        prev = v

    grundy = 0

    for size in reversed(parts):
        grundy = apply(size, grundy)

    if grundy != 0:
        return "Alice"
    return "Bob"


T = int(input())

ans = []
for _ in range(T):
    ans.append(solve())

print("\n".join(ans))
