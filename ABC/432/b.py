#B
X = input()
a = list(X)
a.sort()

if a[0] == '0':
	for i in range (1, len(a)):
		if a[i] != '0':
			a[0], a[i] = a[i], a[0]
			break
		
print("".join(a))