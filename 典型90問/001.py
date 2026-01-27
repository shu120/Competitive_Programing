#001 - Yokan Party
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left = 0
right = L + 1

while right - left > 1:
	mid = (left + right) // 2
	cnt = 0
	last = 0
	for i in A:
		if i - last >= mid:
			cnt += 1
			last = i
	if L - last >= mid:
		cnt += 1

	if cnt >= K + 1:
		left = mid
	else:
		right = mid

print(left)