N = int(input())
C = list(map(int, input().split()))

ans = [N] * N

left = 0

while left < N:
    right = left

    while right + 1 < N and C[right + 1] == C[left]:
        right += 1

    for i in range(left, right + 1):
        if left > 0:
            ans[i] = min(ans[i], i - left + 1)

        if right < N - 1:
            ans[i] = min(ans[i], right - i + 1)

    left = right + 1

print(*ans)
