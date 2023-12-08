class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_point = 0
        max_alt = 0
        for alt in gain:
            next_point = alt + current_point
            max_alt = max(max_alt, next_point)
            current_point = next_point

        return max_alt
