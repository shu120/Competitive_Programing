S = input()

ans = 0
for c in S:
	if c == 'i' or c == 'j':
		ans += 1

print(ans)