#C - Modulo Summation
N = int(input())
a = list(map(int, input().split()))

print(sum(x - 1 for x in a))
