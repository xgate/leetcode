class Solution:
    
    def canPlace(self, flowerbed, i):
        if i == 0:
            return flowerbed[i] == 0 and flowerbed[i+1] == 0
        if i == len(flowerbed)-1:
            return flowerbed[i] == 0 and flowerbed[i-1] == 0
        
        return flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 and n <= 1
        
        l, lens = 0, list()
        for i in range(len(flowerbed)):
            if self.canPlace(flowerbed, i):
                l += 1
            else:
                if l > 0: 
                    lens.append(l)
                    l = 0
        
        if l > 0: lens.append(l)
            
        return sum([int((l+1)/2) for l in lens]) >= n
    