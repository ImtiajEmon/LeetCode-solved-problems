class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # right neighbor greater
            if mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1

            # left neighbor greater
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                l = mid + 1

            # both neighbor are smaller
            else:
                return mid
