class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = [0] * (max(arr)+1010)  #1000 is to handle the neg val
        s = set()

        for i in arr:
            cnt[i+1000] += 1
            s.add(i)

        flag = set()
        for i in s:
            flag.add(cnt[i+1000])

        if len(s) == len(flag):
            return True
        return False
