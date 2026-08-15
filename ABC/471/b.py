from collections import Counter

N = int(input())
S = [input().lower() for _ in range(N)]

ans = Counter(S)

print(max(ans.values()))
