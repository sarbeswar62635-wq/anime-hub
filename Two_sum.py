nums = list(map(int,input("Enter number separated by spaces: ").split()))
target = int(input("Enter Target: "))
seen = {}
for i, num in enumerate(nums):# Gives both index and value
    diff = target - num
    if diff in seen:
        print("Indices:",seen[diff],i)
        break
    seen[num] = i
else:
    print("No solution found.")