class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return
        index = i = j = 0

        while i < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            index = i + 1
            count = j - i
            if count > 1:
                s = str(count)
                for char in s:
                    chars[index] = char
                    index += 1
                #delete the extra char
                for i in range(j-index):
                    chars.pop(index)
                j = index
            i = j
