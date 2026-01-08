H, W = map(int, input().split())
a = [input().strip() for _ in range(H)]

frame = "#" * (W + 2)

print(frame)
for row in a:
	print("#" + row + "#")
print(frame)