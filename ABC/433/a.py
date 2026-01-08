#A
x, y, z = map(int, input().split())

if z == 1:
	print("Yes")
else:
	dif = x - z * y
	d = z - 1
	cond = (dif % d == 0) and (dif // d >= 0)
	print("Yes" if cond else "No")