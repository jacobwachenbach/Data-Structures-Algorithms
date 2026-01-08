

nums = [1,2,3,1]


# Best case O(1) Worse Case O(n)
def add_set():
    my_set = set()

    # Could return after second case or worst 
    # case at the end of the list
    for i in range(len(nums)):
        if nums[i] in my_set:
            return True
        else:
            my_set.add(nums[i])
    return False


# Always O(n)
def len_equal():

    # No Matter list size it will go one by one to 
    # convert to a set making it O(n)
    my_set = set(nums)

    if len(nums) != len(my_set):
        return True
    else:
        return False


print(add_set())
print(len_equal())
