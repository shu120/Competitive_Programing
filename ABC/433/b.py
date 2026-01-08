#B
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
	ans = -1
	for j in range(i - 1, -1, -1):
		if a[j] > a[i]:
			ans = j + 1
			break
	print(ans)