### 관찰

높이는 높을수록 좋다. 거리차이는 많이 날수록 좋다.

높이가 높아도 거리가 좁으면 물의 양이 적을 수 있다.

### 해법

다 해보는 방법이 떠오르지만, O(n^2) 이므로 가능성이 없다.

빠른 방법을 생각해보다가 위에서 한 칸씩 내려오면서 계산하는 방식을 생각을 해봤다. 물론, 꼭 한 칸씩일 필요는 없다.

생각해보면 가장 높은 라인은, 아래로 내려가도 계속 사용 가능하다. 

양쪽의 두 라인 중 낮은 라인의 높이에 맞춰 계산하면 되기때문이다.

결국 최댓값이 되는 후보는 어떤 높이에서 가장 멀리 떨어진 두 개의 라인이다.

```
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
```
