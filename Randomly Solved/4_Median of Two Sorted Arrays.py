class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        merged_arr = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_arr.append(nums1[i])
                i += 1
            else:
                merged_arr.append(nums2[j])
                j += 1
        merged_arr += nums1[i:]
        merged_arr += nums2[j:]

        n = len(merged_arr)
        ans = 0
        if n % 2 == 0:
            ans = (merged_arr[(n//2)-1] + merged_arr[n//2]) / 2
        else:
            ans = merged_arr[n//2]

        return float(ans)
