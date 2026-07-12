class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        
        pos = {}
        i = 1
        for num in arr2:
            if num not in pos:
                pos[num] = i
                i += 1
        print(pos)

        for j in range(len(arr)):
            arr[j] = pos[arr[j]]
        
        return arr


        
