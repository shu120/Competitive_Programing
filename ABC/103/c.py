#C - Modulo Summation
from math import lcm

N = int(input())
a = list(map(int, input().split()))

n = lcm(*a) - 1

ans = sum(n % x for x in a)
print(ans)
