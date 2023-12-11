class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = dict()
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        ans = -1
        temp = -1
        for key in count:
            if count[key] > temp:
                temp = count[key]
                ans = key

        return ans
