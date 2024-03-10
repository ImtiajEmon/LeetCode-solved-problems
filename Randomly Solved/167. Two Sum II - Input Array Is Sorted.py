class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # def binary_search(arr, key):
        #     l, r = 0, len(arr)-1

        #     while l <= r:
        #         mid = (l + r) // 2

        #         if key > arr[mid]:
        #             l = mid + 1
        #         elif key < arr[mid]:
        #             r = mid - 1
        #         else:
        #             return mid

        #     return -1

        # for i in range(len(numbers)-1):
        #     candidate = target - numbers[i]
        #     ret = binary_search(numbers[i+1:], candidate)
        #     if ret != -1:
        #         ans = [i+1, ret+2+i]
        #         return ans

        #======================================================
        # More Optimal Solution
        i, j = 0, len(numbers) - 1
        while i <= j:
            if target > numbers[i] + numbers[j]:
                i += 1
            elif target < numbers[i] + numbers[j]:
                j -= 1
            else:
                return [i+1, j+1]
