from typing import List
import copy


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        dpcd = copy.deepcopy(s)
        for i in range(0, len(s)):
            s[i] = dpcd[len(s) - 1 - i]
