#C - Multiple Clocks
import math
N = int(input())
T = [int(input()) for _ in range(N)]

print(math.lcm(*T))