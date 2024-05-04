class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permutation(nums, ans, idx):
            if idx == len(nums):
                ans.append(nums.copy())

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                permutation(nums, ans, idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        ans = []
        permutation(nums, ans, 0)

        return ans
