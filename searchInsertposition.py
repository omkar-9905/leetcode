for i in range(len(nums)):
    if nums[i] == target:
        return i

nums.append(target)
nums.sort()

ans = nums.index(target)
return ans
