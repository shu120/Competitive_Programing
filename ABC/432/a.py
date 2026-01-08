#A
A, B, C = map(int, input().split())
a = [A, B, C]

x = max(a)
a.remove(x)
y = max(a)
a.remove(y)
z = a[0]

print(x * 100 + y * 10 + z * 1)
