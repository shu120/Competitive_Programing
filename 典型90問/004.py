#004 - Cross Sum（★2）
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

Vert = list(map(sum, zip(*A)))
Horz = list(map(sum, A))

for i in range(H):
	ans = []
	for j in range(W):
		val = Horz[i] + Vert[j] - A[i][j]
		ans.append(str(val))
	print(' '.join(ans))