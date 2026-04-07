H, W = map(int, input().split())

for i in range(1, H + 1):
    r = ""
    for j in range(1, W + 1):
        if i == 1 or i == H or j == 1 or j == W:
            r += "#"
        else:
            r += "."
    print(r)
