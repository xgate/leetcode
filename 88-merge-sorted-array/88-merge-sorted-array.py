class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums = list()
        i, j = 0, m
        while i < m and j < m+n:
            if nums1[i] <= nums1[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums1[j])
                j += 1
        for i in range(i, m):
            nums.append(nums1[i])
        for i in range(j, m+n):
            nums.append(nums1[i])
        for i in range(len(nums)):
            nums1[i] = nums[i]
