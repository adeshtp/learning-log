# Problem: Two Sum
# Approach: Brute force, check all pairs
# Logic: For each number, compare it with the numbers after it until a pair adds
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:  
                    return [i, j]
        return []