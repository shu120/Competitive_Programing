N = int(input())

i = 1
while i <= N:
    if i % 3 != 0:
        print(i)
        i += 1

    else:
        print("Fizz")
        i += 1
