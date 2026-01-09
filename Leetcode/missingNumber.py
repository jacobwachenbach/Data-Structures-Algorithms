
nums = [0,1]


def missing_number():
    
    n = len(nums) + 1
    num_set = set(nums)

    for i in range(n):
        if i not in num_set:
            return i


print(missing_number())