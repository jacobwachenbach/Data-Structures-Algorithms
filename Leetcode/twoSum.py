nums = [2,7,11,15]
target = 9

# O(n)
def dict_method():

    seen = {} # Define a dictionary

    # Loop through with index and number
    for i, n in enumerate(nums):
        # Get sum from target - current number in list
        my_sum = target - n
        # If sum in seen return indices
        if my_sum in seen:
            return [seen[my_sum], i]
        # Else store the number as key and index as value
        seen[n] = i

    print(seen)

# O(n^2)
def brute_force():
    # loop through length of array
    for i in range(len(nums)):
        # Loop through length of array to find target
        for k in range(i+1, len(nums)):
            # If current index + current + 1 = target
            if nums[i] + nums[k] == target:
                return [i, k]

print(dict_method())
print(brute_force())
