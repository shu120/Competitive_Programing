#D
import sys
input = sys.stdin.readline

N = int(input())
clouds = []
for _ in range(N):
	U, D, L, R = map(int, input().split())
	U -= 1; D -= 1; L -= 1; R -= 1
	clouds.append((U, D, L, R))

H = W = 2000
diff = [[0] * (W + 2) for _ in range(H + 2)]

for U, D, L ,R in clouds:
	diff[U][L] += 1
	diff[U][R + 1] -= 1
	diff[D + 1][L] -= 1
	diff[D + 1][R + 1] += 1

for i in range(H + 2):
	row = diff[i]
	for j in range(1, W + 2):
		row[j] += row[j - 1]

for j in range(W + 2):
	for i in range(1, H + 2):
		diff[i][j] += diff[i - 1][j]

cover = diff

flag = 0
one  = [[0] * (W + 1) for _ in range(H + 1)]

for r in range(H):
	row_cover = cover[r]
	row_one = one[r]
	for c in range(W):
		if row_cover[c] == 0:
			flag += 1
		elif row_cover[c] ==1:
			row_one[c] = 1

prefixsum = [[0] * (W + 2) for _ in range(H + 2)]

for r in range(1, H + 2):
	ps_r = prefixsum[r]
	ps_u = prefixsum[r - 1]
	row_one = one[r - 1]
	for c in range(1, W + 2):
		ps_r[c] = (ps_r[c - 1] + ps_u[c] + row_one[c - 1] - prefixsum[r - 1][c - 1])

def rect_sum(ps, r1, c1, r2, c2):
	r1 += 1; c1 += 1; r2 += 1; c2 += 1
	return (ps[r2][c2] - ps[r1 - 1][c2] - ps[r2][c1 - 1] + ps[r1 - 1][c1 - 1])

for U, D, L, R in clouds:
	cnt1 = rect_sum(prefixsum, U, L, D, R)
	print(flag + cnt1)