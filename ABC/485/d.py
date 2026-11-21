N = int(input())
S = input()

idx = {"A": 0, "B": 1, "C": 2}

pref = [0] * 3
mid = [0] * 3
last = [-1] * 3

for i in range(N):
    last[idx[S[i]]] = i

limit = min(last)

ans = 0
right = 1

for left in range(1, N - 1):
    pref[idx[S[left - 1]]] += 1

    while right < N and min(mid) == 0:
        mid[idx[S[right]]] += 1
        right += 1

    if min(pref) > 0 and min(mid) > 0:
        ans += max(0, limit - right + 1)

    if left < right:
        mid[idx[S[left]]] -= 1

print(ans)
