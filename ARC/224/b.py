from math import isqrt
import sys
input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    s = isqrt(4 * N - 1) + 1
    ans.append(str(2 * N - s))

print("\n".join(ans))
