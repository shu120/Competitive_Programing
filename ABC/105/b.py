n = int(input())
for i in range(n // 4 + 1):
	r = n - 4 * i
	if r < 0:
		break
	if r % 7 == 0:
		print("Yes")
		break
else:
	print("No")