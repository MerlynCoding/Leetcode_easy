class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
             result=target-nums[i]
             if result in nums and nums.index(result) !=i:
                return nums.index(result),i
        return[]
            