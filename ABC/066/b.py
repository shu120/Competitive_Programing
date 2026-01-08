#066 B - ss
S = input()

n = len(S)

for i in range(n - 1, 0, -1):
	if i % 2 != 0:
		continue
	half = i // 2
	flag = True

	for j in range(half):
		if S[j] != S[j + half]:
			flag = False
			break

	if flag:
		print(i)
		break
