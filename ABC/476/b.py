N = int(input())
S = input()
T = input()

for i in range(N):
    if T[i] != "*" and S[i] != T[i]:
        print("No")
        exit()

print("Yes")
