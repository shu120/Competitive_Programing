N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print("Yes")
    exit()

left = 0
while A[left] == B[left]:
    left += 1

right = N - 1
while A[right] == B[right]:
    right -= 1

ok = False

if (A[left] == B[right] and A[left + 1:right + 1] == B[left:right]):
    ok = True

if (A[right] == B[left] and A[left:right] == B[left + 1:right + 1]):
    ok = True

print("Yes" if ok else "No")
