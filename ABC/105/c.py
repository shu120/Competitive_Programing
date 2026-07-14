# C - Base -2 Number
N = int(input())

if N == 0:
    print(0)
    exit()

ans = []

while N != 0:
    r = N % 2
    ans.append(str(r))
    N = (N - r) // -2

print("".join(reversed(ans)))
