#C - Make a Rectangle
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
pair = []

for x, cnt in c.items():
	pair += [x] * (cnt // 2)
pair.sort(reverse = True)

if len(pair) >= 2:
	print(pair[0] * pair[1])
else:
	print(0)