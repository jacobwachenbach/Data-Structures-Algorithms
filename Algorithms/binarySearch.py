


nums = [-1,0,3,5,9,12]
target = 9



    

def binarySearch():
    start = 0
    end = len(nums) - 1 


    while start <= end:
        middle = (start + end) // 2

        if nums[middle] == target:
            return middle

        elif nums[middle] > target:
            end = middle - 1
        else:
            start = middle + 1

    return -1

def binaryRecursion(nums, target, start, end):

    if start > end:
        return -1
    middle = (start + end) // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] > target:
        return binaryRecursion(nums, target, start, middle - 1)
    else:
        return binaryRecursion(nums, target, middle + 1, end)
        
print(binarySearch())
print(binaryRecursion(nums, target, 0, len(nums) - 1))
