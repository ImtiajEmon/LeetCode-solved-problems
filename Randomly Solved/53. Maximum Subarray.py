class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]

        # mid = len(nums)//2

        # lss = self.maxSubArray(nums[:mid])
        # rss = self.maxSubArray(nums[mid:])

        # sum = 0
        # left_sum, right_sum = -1e9, -1e9

        # #for left sum
        # for i in range(mid-1, -1, -1):
        #     sum += nums[i]
        #     left_sum = max(sum, left_sum)

        # #for right sum
        # sum = 0
        # for i in range(mid, len(nums), 1):
        #     sum += nums[i]
        #     right_sum = max(sum, right_sum)

        # return max(lss, rss, left_sum+right_sum)

        #==========================================================
        # More optimal solution

        ans = -1e9
        sum = 0

        for num in (nums):
            sum += num
            ans = max(ans, sum)
            if sum < 0:
                sum = 0

        return ans
