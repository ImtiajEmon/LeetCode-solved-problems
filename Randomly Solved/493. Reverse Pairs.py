class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeAndCount(arr1, arr2):
            # Count the inversions
            nonlocal ans
            i, j = 0, 0
            
            while i < len(arr1) and j < len(arr2):
                if arr1[i] > 2 * arr2[j]:
                    ans += len(arr1) - i
                    j += 1
                else:
                    i += 1
                    
            # Now merge the arrays and return
            i, j = 0, 0
            merged_arr = []
            
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged_arr.append(arr1[i])
                    i += 1
                else:
                    merged_arr.append(arr2[j])
                    j += 1
                    
            merged_arr += arr1[i:]
            merged_arr += arr2[j:]
            
            return merged_arr
            
            
        
        def count_inverse(arr):
            if len(arr) == 1:
                return arr
                
            mid = len(arr) // 2
            
            left_arr = count_inverse(arr[:mid])
            right_arr = count_inverse(arr[mid:])
            
            return mergeAndCount(left_arr, right_arr)
        
        ans = 0   
        count_inverse(nums)
        return ans
