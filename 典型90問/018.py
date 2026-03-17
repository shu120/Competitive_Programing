#018 - Statue of Chokudai（★3）
import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    E = int(input())

    theta = 2 * math.pi * E / T

    y = - (L / 2) * math.sin(theta)
    z = (L / 2) * (1 - math.cos(theta))

    d = math.sqrt(X ** 2 + (Y - y) ** 2)

    angle = math.degrees(math.atan2(z, d))

    print(angle)
