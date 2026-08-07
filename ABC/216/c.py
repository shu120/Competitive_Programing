# C - Many Balls
N = int(input())
S = []

while N != 0:
    if N % 2 == 0:
        N //= 2
        S.append("B")
    else:
        N -= 1
        S.append("A")

print("".join(reversed(S)))
