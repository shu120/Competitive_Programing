#027 - Sign Up Requests （★2）
N = int(input())
S = [input() for _ in range(N)]

seen = set()
for i in range(N):
    if S[i] not in seen:
        print(i + 1)
        seen.add(S[i])
