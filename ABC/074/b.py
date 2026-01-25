#B - Collecting Balls (Easy Version)
N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0

for i in x:
	ans += min(i, abs(K - i))

print(ans * 2)