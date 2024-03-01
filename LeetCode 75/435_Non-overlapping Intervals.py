class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[1])
        cnt = 0

        last_end = -1e5
        for intv in intervals:
            if intv[0] >= last_end:
                last_end = intv[1]
                cnt += 1

        return len(intervals) - cnt
