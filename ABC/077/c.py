#C - Snuke Festival
from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0

for i in B:
    left = bisect_left(A, i)
    right = N - bisect_right(C, i)
    ans += left * right

print(ans)
