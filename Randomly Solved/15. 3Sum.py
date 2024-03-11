class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 candidate = [nums[i], nums[j], nums[k]]
        #                 candidate.sort()
        #                 if candidate not in ans:
        #                     ans.append(candidate)

        # return ans

        # Optimal Solution

        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]

            while l < r:
                if target > nums[l] + nums[r]:
                    l += 1
                elif target < nums[l] + nums[r]:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ans
