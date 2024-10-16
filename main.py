from typing import List
def twoSum(nums: List[int], target: int) -> List[int]: 
    
    for x in range(0,len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x,y]
    return []

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))