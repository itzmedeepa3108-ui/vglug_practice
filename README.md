# vglug_practice
# Python Programming Practice Exercises

This repository contains clear, human-style Python implementations for common programmatic problem-solving exercises. Each program focuses on straightforward logic without relying on extra function overhead or complex error wrappers.

---

## Table of Contents
1. [Palindrome Number Check](#1-palindrome-number-check)
2. [Power of Two Check](#2-power-of-two-check)
3. [Reduce a Number to Zero](#3-reduce-a-number-to-zero)
4. [Count Days Spent Together](#4-count-days-spent-together)

---

## 1. Palindrome Number Check
**Problem Statement:** Given an integer `x`, determine if it reads the same forward and backward. Returns `True` if it is a palindrome and `False` otherwise. Note that negative numbers and numbers with trailing zeros (except `0`) are not palindromes.

### Logic Flow
- Filter out numbers less than zero immediately.
- Reverse the number mathematically by isolating the last digit using modulo (`% 10`) and shifting using floor division (`// 10`).
- Compare the original number to the fully reversed number.

```python
x = int(input("Enter a number: "))
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
```

---

## 2. Power of Two Check
**Problem Statement:** Given an integer `n`, return `True` if it is a power of two. Otherwise, return `False`. An integer `n` is a power of two if there exists an integer `x` such that \(n == 2^x\).

### Logic Flow
- Any number less than or equal to `0` cannot be a power of two.
- As long as the number is completely even (`n % 2 == 0`), continually divide it by 2.
- If it reduces perfectly down to `1`, the original number was a power of two.

```python
n = int(input("Enter a number: "))

if n <= 0:
    print(False)
else:
    while n % 2 == 0:
        n //= 2

    if n == 1:
        print(True)
    else:
        print(False)
```

---

## 3. Reduce a Number to Zero
**Problem Statement:** Given an integer `num`, return the total number of steps required to reduce it down to zero. In one single step:
- If the current number is **even**, divide it by `2`.
- If the current number is **odd**, subtract `1` from it.

### Logic Flow
- Use a `while` loop that increments a counter on every pass until the target integer hits zero.
- Evaluate the number's parity using `% 2` at every step to apply the correct operational path.

```python
num = int(input("Enter a number: "))
steps = 0

while num > 0:
    if num % 2 == 0:
        num //= 2
    else:
        num -= 1
    steps += 1

print(steps)
```

---

## 4. Count Days Spent Together
**Problem Statement:** Alice and Bob are traveling to Rome. Given 4 string boundaries in the format `"MM-DD"` (`arriveAlice`, `leaveAlice`, `arriveBob`, `leaveBob`), calculate the exact inclusive overlap of days they spent in the city together during a standard non-leap calendar year.

### Logic Flow
- Maps each `"MM-DD"` date boundary into an absolute day integer from `1` to `365` using an array tracking days per month.
- Pinpoints the intersection interval by targeting the latest arrival day (`max`) and the earliest departure day (`min`).
- Outputs the complete input configuration alongside the outcome dynamically.

```python
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

arrive_alice = input("Enter arriveAlice: ")
leave_alice = input("Enter leaveAlice: ")
arrive_bob = input("Enter arriveBob: ")
leave_bob = input("Enter leaveBob: ")

# Convert Alice's dates to absolute day index numbers
month, day = int(arrive_alice[0:2]), int(arrive_alice[3:5])
alice_start = sum(days_in_months[:month - 1]) + day

month, day = int(leave_alice[0:2]), int(leave_alice[3:5])
alice_end = sum(days_in_months[:month - 1]) + day

# Convert Bob's dates to absolute day index numbers
month, day = int(arrive_bob[0:2]), int(arrive_bob[3:5])
bob_start = sum(days_in_months[:month - 1]) + day

month, day = int(leave_bob[0:2]), int(leave_bob[3:5])
bob_end = sum(days_in_months[:month - 1]) + day

# Calculate overlap window boundaries
latest_start = max(alice_start, bob_start)
earliest_end = min(alice_end, bob_end)

if latest_start <= earliest_end:
    together_days = earliest_end - latest_start + 1
else:
    together_days = 0

# Formatted console output display template
print(f'Input: arriveAlice = "{arrive_alice}", leaveAlice = "{leave_alice}", arriveBob = "{arrive_bob}", leaveBob = "{leave_bob}" Output: {together_days}')
```
