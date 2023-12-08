class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #I implement the idea of prefix sum. if i choose index i
        #then left_sum = pref_sum[i-1] & right_sum = pref_sum[last_idx] - pref_sum[i]
        prefix_sum = [0] # deafult pref_sum[0] = 0 in case of i-1
        i = 1
        for num in nums:
            prefix_sum.append(prefix_sum[i-1] + num)
            i += 1

        n = len(prefix_sum)
        for i in range(1, n):
            if prefix_sum[i-1] == prefix_sum[n-1] - prefix_sum[i]:
                return i-1 # returning to 0 base indexing
            
        return -1
