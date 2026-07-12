import sys

input = sys.stdin.readline


def solve(k: int) -> int:
    for m in range(1, 101):
        n = k * m

        if "00" in str(n):
            return n

    return -1


t = int(input())
ans = []

for _ in range(t):
    k = int(input())
    ans.append(str(solve(k)))

print("\n".join(ans))
