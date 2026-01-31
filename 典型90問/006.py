#006 - Smallest Subsequence（★5）
N, K = map(int, input().split())
S = input()

nex = [[N] * 26 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
	for j in range(26):
		nex[i][j] = nex[i + 1][j]
	nex[i][ord(S[i]) - ord('a')] = i

ans = ''
pos = 0
for i in range(K):
	for c in range(26):
		nx = nex[pos][c]
		if N - nx >= K - i:
			ans += chr(ord('a') + c)
			pos = nx + 1
			break

print(ans)