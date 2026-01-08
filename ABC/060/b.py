#ver.1
A, B, C = map(int, input().split())

for i in range(B):
	if(A * i) % B == C:
		print("YES")
		break
else:
	print("NO")

#ver.2
A, B, C = map(int, input().split())

for i in range(B):
	if(A * i) % B == C:
		print("YES")
		break
	elif i == B - 1:
		print("NO")
