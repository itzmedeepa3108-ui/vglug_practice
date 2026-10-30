x = int(input())
original = x
reversed_num = 0
if x < 0:
    print(False)
else:
    while x > 0:
        last_digit = x % 10
        reversed_num = (reversed_num * 10) + last_digit
        x //= 10
    if original == reversed_num:
        print(True)
    else:
        print(False)
