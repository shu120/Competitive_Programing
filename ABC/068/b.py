#ABC068 B - Break Number
N = int(input())

ans = 1
while ans * 2 <= N:
	ans *= 2

print(ans)