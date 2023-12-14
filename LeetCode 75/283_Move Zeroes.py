class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                j = i
                while j > 0+cnt:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                    j -= 1
                cnt += 1
