class Solution:            
    def find(self, nums, start, f):
        for i in range(start, len(nums)):
            if f(nums[i]):
                return i
        return -1
            
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nz = 0
        while True:            
            z = self.find(nums, z, lambda x: x == 0)
            nz = self.find(nums, nz, lambda x: x != 0)
            if z == -1 or nz == -1:
                break
            if nz > z:
                nums[z] = nums[nz]
                nums[nz] = 0
                z += 1
            else:
                nz += 1
