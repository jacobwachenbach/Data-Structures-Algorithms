
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Problem
# 1. Array of integers nums
# 2. Integer target
# 3. return indices of the two numbers such that they add up to target

# Assumptions:
# 1. each input would have exactly one solution
# 2. you may not use the same element twice

nums = [11,15,2,7]
target = 9

# O(n)
def dict_method():

    seen = {} # Define a dictionary

    # Loop through with index and number
    for i, n in enumerate(nums):
        # Get diff from target - current number in list
        diff = target - n
        # If diff in seen return indices
        if diff in seen:
            return [seen[diff], i]
        # Else store the number as key and index as value
        seen[n] = i

seen = {
    # key : value
    11 : 0,
    15 : 1,
     2 : 2,
}




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
