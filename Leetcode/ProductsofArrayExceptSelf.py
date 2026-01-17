
import math

nums = [1,2,4,6]




product_map = {}

result = []

product = 1

start = 0
end = len(nums)

for i in range(len(nums)):

    product = 1
    
    prefix = nums[start:i]
    suffix = nums[i + 1:end]

    sum1 = math.prod(nums[start: i])
    sum2 = math.prod(nums[i + 1:end])

    res = sum1 * sum2

    result.append(res)
    
    

print(result)