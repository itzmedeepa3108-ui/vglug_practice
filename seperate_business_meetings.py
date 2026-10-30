days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arrive_alice = input("Enter arriveAlice: ")
leave_alice = input("Enter leaveAlice: ")
arrive_bob = input("Enter arriveBob: ")
leave_bob = input("Enter leaveBob: ")
month, day = int(arrive_alice[0:2]), int(arrive_alice[3:5])
alice_start = sum(days_in_months[:month - 1]) + day

month, day = int(leave_alice[0:2]), int(leave_alice[3:5])
alice_end = sum(days_in_months[:month - 1]) + day

month, day = int(arrive_bob[0:2]), int(arrive_bob[3:5])
bob_start = sum(days_in_months[:month - 1]) + day

month, day = int(leave_bob[0:2]), int(leave_bob[3:5])
bob_end = sum(days_in_months[:month - 1]) + day

latest_start = max(alice_start, bob_start)
earliest_end = min(alice_end, bob_end)

if latest_start <= earliest_end:
    together_days = earliest_end - latest_start + 1
else:
    together_days = 0

print(together_days)
