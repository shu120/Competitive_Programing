from collections import Counter

N = int(input())
C = list(map(int, input().split()))

cnt = Counter(C)

print(N - max(cnt.values()))
