from typing import List

nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if i is j:
                    pass
                else:
                    if nums[i] + nums[j] is target:
                        return [i, j]

sol1 = Solution()

print(sol1.twoSum(nums, target))