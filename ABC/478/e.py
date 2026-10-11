N = int(input())
Q = list(map(int, input().split()))
MOD = 998244353

stack = []
ans = 1

for i, curr in enumerate(Q, start = 1):
    while stack and stack[-1][0] < curr:
        stack.pop()

    if i > 1:
        if stack:
            ans *= i - stack[-1][1]
        else:
            ans *= i - 1

        ans %= MOD

    stack.append((curr, i))

print(ans)
