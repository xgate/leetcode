class Solution:
    def maxArea(self, height: List[int]) -> int:
        hd = dict()
        for i in range(len(height)):
            indexes = hd.get(height[i])
            if not indexes:
                hd[height[i]] = (i, i)
            else:
                hd[height[i]] = (min(i, indexes[0]), max(i, indexes[1]))

        ans = 0
        l, r = 100001, 0
        for h in sorted(hd.keys(), reverse=True):
            l = min(l, hd[h][0])
            r = max(r, hd[h][1])
            ans = max(ans, (r - l) * min(height[l], height[r]))

        return ans
