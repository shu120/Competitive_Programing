N, X = input().split()
N = int(N)
S = [input() for _ in range(N)]

idx = "ABCDE".index(X)

for s in S:
    if s[idx] == "o":
        print("Yes")
        break
else:
    print("No")
