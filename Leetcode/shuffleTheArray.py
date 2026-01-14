


nums = [2,5,1,3,4,7]
n = 3
new_array = []
for i in range(0, n):
    new_array.extend([nums[i], nums[n + i]])
print(new_array)