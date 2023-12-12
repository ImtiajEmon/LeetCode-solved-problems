class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import math
        if len(nums) < 3:
            return False

        left_min = []
        right_max = []
        temp = math.inf

        for num in nums:
            temp = min(temp, num)
            left_min.append(temp)

        temp = -math.inf
        for i in range(len(nums)-1, -1, -1):
            temp = max(temp, nums[i])
            right_max.append(temp)
        right_max.reverse()

        for i in range(len(nums)):
            if left_min[i] < nums[i] and nums[i] < right_max[i]:
                return True

        return False
        
