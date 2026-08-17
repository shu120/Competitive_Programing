# E - Amusement Park
N, K = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)

A.append(0)
ans = 0

for i in range(N):
    cnt = i + 1
    diff = A[i] - A[i + 1]
    need = cnt * diff

    if need <= K:
        high = A[i]
        low = A[i + 1] + 1

        s = (high + low) * (high - low + 1) // 2
        ans += s * cnt

        K -= need

    else:
        q = K // cnt
        r = K % cnt

        high = A[i]
        low = A[i] - q + 1

        s = (high + low) * q // 2
        ans += s * cnt

        ans += (A[i] - q) * r

        break

print(ans)
