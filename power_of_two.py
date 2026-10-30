n = int(input())
if n <= 0:
    print(False)
else:
    while n % 2 == 0:
        n //= 2
    if n == 1:
        print(True)
    else:
        print(False)
