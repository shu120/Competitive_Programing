#abc076a
r = int(input())
g = int(input())
print(2 * g - r)

#abc076b
n = int(input())
k = int(input())

i = 1

for _ in range(n):
	if i * 2 < i + k:
		i *= 2
	else:
		i += k
print(i)

#abc077a
a, b, c = input()
d, e, f = input()

if a == f and b == e and c == d:
	print("YES")
else:
	print("NO")

#abc077b
import math
n = int(input())
x = int(math.sqrt(n))
print(x * x)

#abc078a
x, y = input().split()

if str(x) > str(y):
	print(">")
elif str(x) < str(y):
	print("<")
else:
	print("=")

#abc078b
x, y, z = map(int, input().split())
print(int((x - z) / (y + z)))

#abc106b
N = int(input())

ans = 0
for i in range(1, N+1, 2):
	div = 0
	for j in range(1, i+1):
		if i % j == 0:
			div += 1
	if div == 8:
		ans += 1
print(ans)

#abc068b
N = int(input())

cand = []
for i in range(1, N+1):
	count = 0
	x = i
	while x % 2 == 0:
		x //= 2
		count += 1
	cand.append((count, i))
print(max(cand)[1])

#abc136b
N = int(input())

count = 0
for i in range (1, N+1):
	if len(str(i)) % 2 == 1:
		count += 1
print(count)