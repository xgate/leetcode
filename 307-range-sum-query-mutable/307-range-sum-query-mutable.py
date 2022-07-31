class NumArray:
    
    def buildTree(self, left, right):
        if left == right:
            return self.seg[(left, right)]
        mid = left+int((right-left)/2)
        self.seg[(left, right)] = self.buildTree(left, mid)+self.buildTree(mid+1, right)
        return self.seg[(left, right)]
    
    def updateTree(self, left, right, index, val):
        if left == right and index == left:
            self.seg[(left, right)] = val
        else:
            mid = left+int((right-left)/2)
            if index <= mid:
                self.seg[(left, right)] = self.updateTree(left, mid, index, val)+self.seg[(mid+1, right)]
            else:
                self.seg[(left, right)] = self.seg[(left, mid)]+self.updateTree(mid+1, right, index, val)
        
        return self.seg[(left, right)]
    
    def queryTree(self, left, right, targetLeft, targetRight):
        if targetLeft > right or targetRight < left:
            return 0
        if targetLeft <= left and targetRight >= right:
            return self.seg[(left, right)]
        mid = left+int((right-left)/2)
        return self.queryTree(left, mid, targetLeft, targetRight) + self.queryTree(mid+1, right, targetLeft, targetRight)

    def __init__(self, nums: List[int]):
        self.seg = dict()
        self.right = len(nums)-1
        for i in range(len(nums)):
            self.seg[(i, i)] = nums[i]
        self.buildTree(0, self.right)
        
    def update(self, index: int, val: int) -> None:
        self.updateTree(0, self.right, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.queryTree(0, self.right, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
