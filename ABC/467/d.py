T = int(input())

for _ in range(T):
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = map(int, input().split())

    dx1 = Qx - Px
    dy1 = Qy - Py
    c1 = Qx**2 + Qy**2 - Px**2 - Py**2

    dx2 = Sx - Rx
    dy2 = Sy - Ry
    c2 = Sx**2 + Sy**2 - Rx**2 - Ry**2

    if dx1 * dy2 != dy1 * dx2:
        print("Yes")
        continue

    if dx1 * c2 == dx2 * c1 and dy1 * c2 == dy2 * c1:
        print("Yes")
    else:
        print("No")
