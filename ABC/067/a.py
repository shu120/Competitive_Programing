#ABC067 A - Sharing Cookies
A, B = map(int, input().split())

S = A + B
if A % 3 == 0 or B % 3 == 0 or S % 3 == 0:
	print("Possible")
else:
	print("Impossible")