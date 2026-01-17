


nums = [0,3,2,5,4,6,1,1]
if not nums:
    print(0)
    exit
nums.sort()
longest_streak = 1
current_streak = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        continue
    if nums[i] == nums[i-1] + 1:
        current_streak += 1
    else:
        longest_streak = max(longest_streak, current_streak)
        current_streak = 1


print(max(longest_streak, current_streak))