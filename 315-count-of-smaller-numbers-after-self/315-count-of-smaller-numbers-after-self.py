class Solution:
    
    def mergeSort(self, numsAndIndexes, countDict):
        if len(numsAndIndexes) == 1:            
            return numsAndIndexes
        
        mid = int(len(numsAndIndexes)/2)
        left = self.mergeSort(numsAndIndexes[:mid], countDict)
        right = self.mergeSort(numsAndIndexes[mid:], countDict)
        
        merged = list()
        li = ri = smaller = 0
        while li < len(left) and ri < len(right):
            if left[li][0] < right[ri][0]:                
                merged.append(left[li])
                countDict[left[li][1]] += smaller
                li += 1
            elif left[li][0] > right[ri][0]:
                merged.append(right[ri])
                smaller += 1
                ri += 1
            else:
                num = left[li][0]
                count = 0
                lbreak = rbreak = False
                while True:
                    if li < len(left) and left[li][0] == num:
                        merged.append(left[li])
                        countDict[left[li][1]] += smaller    
                        li += 1
                    else:
                        lbreak = True
                
                    if ri < len(right) and right[ri][0] == num:
                        merged.append(right[ri])
                        ri += 1
                        count += 1   
                    else:
                        rbreak = True
                    
                    if lbreak and rbreak:
                        break
                    
                smaller += count
                
        while ri < len(right):
            merged.append(right[ri])
            ri += 1
            
        while li < len(left):
            merged.append(left[li])
            countDict[left[li][1]] += smaller
            li += 1
            
        return merged
        
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]            
        
        countDict = dict()
        for i in range(len(nums)):
            countDict[i] = 0
        
        self.mergeSort([(nums[i], i) for i in range(len(nums))], countDict)
        
        return [countDict.get(k, 0) for k in sorted(countDict.keys())]
