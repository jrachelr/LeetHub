class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        set_arr = set(arr)
        
        for num in arr:
            if num + 1 in set_arr:
                count += 1
        
        return count