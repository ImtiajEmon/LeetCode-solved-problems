#solution - 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pref_prod = 1
        for i in range(len(nums)-1):
            pref_prod *= nums[i]
            ans[i+1] = pref_prod

        suff_prod = 1
        for i in range(len(nums)-1, 0, -1):
            suff_prod *= nums[i]
            ans[i-1] *= suff_prod

        return ans

#===================================================================================
#solution - 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1] * (len(nums)+1)
        suff_prod = [1] * (len(nums)+2) #idx 0 & last remain 1

        i, j = 0, len(nums)-1
        while j >= 0:
            pref_prod[i+1] = pref_prod[i] * nums[i]
            suff_prod[j+1] = suff_prod[j+2] * nums[j]
            i += 1
            j -= 1

        ans = []
        for i in range(1, len(pref_prod)):
            ans.append(pref_prod[i-1] * suff_prod[i+1])

        return ans
