


nums = [1,2,2,3,3,3]
k = 2

count = {}
freq = []

for num in nums:
    count[num] = count.get(num, 0) + 1

sorted_keys = sorted(count, key=count.get, reverse=True)

# 3. Slice the list to get the top k
result = sorted_keys[:k]

print(result)
    
    