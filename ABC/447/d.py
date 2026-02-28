S = input()

a = 0
ab = 0
abc = 0

for c in S:
	if c == 'A':
		a += 1
	elif c == 'B':
		if a > 0:
			a -= 1
			ab += 1
	else:
		if ab > 0:
			ab -= 1
			abc += 1

print(abc)