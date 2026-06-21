X, Y = map(int, input().split())

if X % 16 == 0 and Y % 9 == 0:
    print("Yes")
else:
    print("No")
