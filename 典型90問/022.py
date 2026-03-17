#022 - Cubic Cake（★2）
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B, C = map(int, input().split())
g = gcd(A, gcd(B, C))
ans = A // g + B // g + C // g - 3
print(ans)
