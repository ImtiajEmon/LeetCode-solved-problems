class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

        #=========================================
        # Another solution
        # def partition(l, r):
        #     pivot = nums[l]
        #     i, j = l, l + 1

        #     while j <= r:
        #         if nums[j] <= pivot:
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]
        #         j += 1

        #     nums[i], nums[l] = nums[l], nums[i]

        #     return i

        # def quickSelect(l, r):
        #     if l <= r:
        #         p = partition(l, r)
        #         index_in_arr = len(nums) - k

        #         if p > index_in_arr:
        #             return quickSelect(l, p - 1)
        #         elif p < index_in_arr:
        #             return quickSelect(p + 1, r)
        #         else:
        #             return nums[p]


        return quickSelect(0, len(nums)-1)
