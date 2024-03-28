class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [pair for pair in zip(nums1, nums2)]
        pairs.sort(key = lambda p: p[1], reverse = True)

        res = 0
        min_heap = []
        n1_sum = 0

        for n1, n2 in pairs:
            n1_sum += n1
            heapq.heappush(min_heap, n1)

            if  len(min_heap) > k:
                n1_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                res = max(res, n1_sum * n2)


        return res
