class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        for num in nums1:
            if num not in answer[0] and num not in nums2:
                answer[0].append(num)

        for num in nums2:
            if num not in answer[1] and num not in nums1:
                answer[1].append(num)
            
        return answer
