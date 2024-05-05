class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash_map = {n: 0 for n in nums}

        for n in nums:
            hash_map[n] += 1

        res = []
        perm = []

        def unique_permutation():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for key in hash_map:
                if hash_map[key] > 0:
                    perm.append(key)
                    hash_map[key] -= 1

                    unique_permutation()

                    perm.pop()
                    hash_map[key] += 1

        unique_permutation()
        return res
