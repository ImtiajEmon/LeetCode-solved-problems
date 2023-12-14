class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        def binary_search(n):
            i = 0
            j = len(nums) - 1
            while i <= j:
                mid = (i+j) // 2
                if n == nums[mid]:
                    return mid
                elif n > nums[mid]:
                    i = mid+1
                else:
                    j = mid-1
            return -1

        nums.sort()
        cnt = 0
        i = 0
        while i < len(nums):
            target = k - nums[i]
            j = binary_search(target)
            if j != -1 and j != i:
                cnt += 1
                nums.pop(i)
                nums.pop(j-1)
            else:
                i += 1
        
        return cnt
