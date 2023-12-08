class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        temp_sum = 0
        for i in range(k):
            temp_sum += nums[i]

        max_sum = temp_sum
        for i in range(k,len(nums)):
            temp_sum = temp_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, temp_sum)

        ans = round(max_sum / k, 5)
        return ans
        
