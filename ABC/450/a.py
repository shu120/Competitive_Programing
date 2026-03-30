N = int(input())
for i in range(N, 0, -1):
    print(i, end = "")
    if i != 1:
        print(",", end = "")
