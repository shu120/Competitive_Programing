from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

common = Counter(S[0])

for i in range(1, n):
	common &= Counter(S[i])

ans = ""
for ch in sorted(common.keys()):
	ans += ch * common[ch]

print(ans)