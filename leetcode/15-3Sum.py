from typing import List
from itertools import combinations

nums = [-1, 0, 1, 2, -1, -4]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = list()
        if len(nums) < 3:
            return []
        cmbs = list(combinations(nums, 3))
        for cmb in cmbs:
            if sum(cmb) == 0:
                temp.append(list(cmb))
		ret = temp
        return ret


sol1 = Solution()

print(sol1.threeSum(nums))
