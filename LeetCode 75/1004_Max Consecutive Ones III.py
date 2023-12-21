class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        zero_idx = 0
        one_cnt = 0
        first = True

        for i in range(len(nums)):
            if nums[i] == 1:
                one_cnt += 1
            elif nums[i] == 0:
                if first:
                    zero_idx = i
                    first = False
                if k > 0:
                    one_cnt += 1
                    k -= 1
                elif k == 0:
                    ans = max(ans, one_cnt)
                    while nums[zero_idx] == 1:
                        zero_idx += 1
                    one_cnt = i - zero_idx
                    zero_idx += 1

        ans = max(ans, one_cnt)
        return ans
