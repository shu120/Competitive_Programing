A = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = []
for _ in range(n):
	b.append(int(input()))

marked = [[False] * 3 for _ in range(3)]

for i in range(3):
	for j in range(3):
		if A[i][j] in b:
			marked[i][j] = True

bingo = False
for i in range(3):
	if all(marked[i][j] for j in range(3)):
		bingo = True
for j in range(3):
	if all(marked[i][j] for i in range(3)):
		bingo = True
if all(marked[i][i] for i in range(3)):
	bingo = True
if all(marked[i][2 - i] for i in range(3)):
	bingo = True

print("Yes" if bingo else "No")