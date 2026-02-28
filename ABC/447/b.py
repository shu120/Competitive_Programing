from collections import Counter
S = input()

cnt = Counter(S)
mx = max(cnt.values())
print("".join(c for c in S if cnt[c] != mx))
