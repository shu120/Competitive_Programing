#D - 2017-like Number
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

MAX = 10 ** 5

prime = [True] * (MAX + 1)
prime[0] = prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False

like = []
for i in range(1, MAX + 1):
    if prime[i] and prime[(i + 1) // 2]:
        like.append(i)


Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    ans = bisect_right(like, R) - bisect_left(like, L)
    print(ans)
