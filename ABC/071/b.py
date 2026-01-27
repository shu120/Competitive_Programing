#B - Not Found
S = input()

s = set(S)
for c in range(ord('a'), ord('z') + 1):
	ch = chr(c)
	if ch not in s:
		print(ch)
		break
else:
	print("None")