# E - Placing Rectangles
from itertools import permutations
X, Y, A, B, C = map(int, input().split())

for a, b, c in permutations([A, B, C]):
    for x, y in [(X, Y), (Y, X)]:
        ha = (a + x - 1) // x
        hb = (b + x - 1) // x
        hc = (c + x - 1) // x

        if ha + hb + hc <= y:
            print("Yes")
            exit()

        h = y - ha

        if h > 0:
            wb = (b + h - 1) // h
            wc = (c + h - 1) // h

            if wb + wc <= x:
                print("Yes")
                exit()
print("No")
