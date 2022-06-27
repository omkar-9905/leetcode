di = {}

if len(nums) == 1:
    print(int(nums))
else:
    for i,j in enumerate(nums):
        di[nums.count(j)] = j

print(di[1])
