class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sm = sum(arr)
        if sm % 3 != 0:
            return False
        
        lsum = found = 0
        average = int(sm/3)
        for i in range(len(arr)):
            lsum += arr[i]
            if lsum == average:
                lsum = 0
                found += 1            
        
        return found >= 3
