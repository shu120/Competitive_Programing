#C - 4-adjacent
N = int(input())
a = list(map(int, input().split()))

mlt4 = 0
mlt2 = 0
odd = 0

for i in a:
	if i % 4 == 0:
		mlt4 += 1
	elif i % 2 == 0:
		mlt2 += 1
	else:
		odd += 1

if mlt2 == 0:
	ok = (odd <= mlt4 + 1)
else:
	ok = (odd <= mlt4)

print("Yes" if ok else "No")