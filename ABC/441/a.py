#A - Black Square
P, Q = map(int, input().split())
X, Y = map(int, input().split())

if P <= X <= P + 99 and Q <= Y <= Q + 99:
	print("Yes")
else:
	print("No")