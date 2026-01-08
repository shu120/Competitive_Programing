#B
N, M = map(int, input().split())
kinds = [tuple(map(int, input().split())) for _ in range(N)]

sumb = [0] * (M + 1)
cnt = [0] * (M + 1)

for a, b in kinds:
	sumb[a] += b
	cnt[a] += 1
for i in range(1, M + 1):
	print(sumb[i] / cnt[i])