class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for j in range(1, len(nums)):
            if nums[j-1] + 1 == nums[j]:
                sum += nums[j]
            else:
                break
                
        while sum in nums:
            sum += 1
            
        return sum
