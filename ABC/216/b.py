# B - Same Name
N = int(input())
name = set()

for _ in range(N):
    S, T = input().split()

    if (S, T) in name:
        print("Yes")
        exit()
    name.add((S, T))

print("No")
