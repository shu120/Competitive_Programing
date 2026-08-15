A, B = map(int, input().split())

if A + B == 9 or A - B == 9 or A * B == 9 or A == 9 * B:
    print("Nine")
else:
    print("Nein")
