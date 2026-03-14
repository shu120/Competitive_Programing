import sys
input = sys.stdin.readline

ALPHABET_SIZE = 26

N, L, R = map(int, input().split())
S = input()

cnt = [0] * ALPHABET_SIZE
ans = 0

for i in range(N):

	add = i - L
	remove = i - R - 1

	if add >= 0:
		cnt[ord(S[add]) - ord('a')] += 1

	if remove >= 0:
		cnt[ord(S[remove]) - ord('a')] -= 1

	ans += cnt[ord(S[i]) - ord('a')]

print(ans)
