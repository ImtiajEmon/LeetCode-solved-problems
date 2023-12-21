class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = True
        idx = 0
        cnt = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if flag:
                    idx = i
                    flag = False
                else:
                    ans = max(ans, cnt)
                    cnt = i - idx - 1
                    idx = i
            else:
                cnt += 1

        if flag:
            ans = cnt - 1
        else:
            ans = max(ans, cnt)
        
        return ans
